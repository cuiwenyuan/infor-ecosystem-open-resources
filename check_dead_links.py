#!/usr/bin/env python3
"""
Infor 生态开放资源导航站 - 死链检测脚本
扫描 docs/ 下所有 Markdown 文件中的链接，检测失效链接并生成报告。

用法：
  python check_dead_links.py --docs-dir docs --output dead_links_report.md
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("正在安装 requests...", flush=True)
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests


# ── 已知反爬域名（跳过检测，避免误报）──
# 这些站点对无头检测返回 403 / 超时 / 重定向环，但本身存活，
# 死链巡检时直接跳过，避免误报拖慢扫描。
SKIP_DOMAINS = {
    "github.com",
    "stackoverflow.com",
    "douyin.com",
    "www.douyin.com",
    "mp.weixin.qq.com",
    "wx.zsxq.com",
    # 反爬误报域名（2026-07-08 补充）：社交 / 社区 / 评测类站点
    "linkedin.com",       # LinkedIn 全站（含 www. 子域）拦截无头请求
    "zhihu.com",          # 知乎 搜索 / 话题页
    "g2.com",             # G2 用户评测聚合
    "customerfx.com",     # Customer FX 社区 / 博客
}


def should_skip(url: str) -> bool:
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    return any(domain == d or domain.endswith("." + d) for d in SKIP_DOMAINS)


# ── 从 Markdown 提取所有链接 ─

def extract_links(file_path: Path):
    """
    返回 [(line_no, url, is_external), ...]
    is_external: True = http/https，False = 内部相对路径
    """
    results = []
    link_re = re.compile(r"\[[^\]]*\]\s*\((\s*[^)\s]+?\s*)\)")
    ref_re = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)\s*$", re.MULTILINE)
    angle_re = re.compile(r"<(https?://[^>]+)>")
    bare_re = re.compile(r"(?<![\(\[])(https?://\S+)(?![\)\]])")

    with open(file_path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            for m in link_re.finditer(line):
                url = m.group(1).strip()
                is_ext = url.startswith(("http://", "https://"))
                results.append((line_no, url, is_ext))
            for m in ref_re.finditer(line):
                url = m.group(1).strip()
                is_ext = url.startswith(("http://", "https://"))
                results.append((line_no, url, is_ext))
            for m in angle_re.finditer(line):
                url = m.group(1).strip()
                results.append((line_no, url, True))
            for m in bare_re.finditer(line):
                url = m.group(1).strip().rstrip(".,;)")
                if not any(r[1] == url for r in results if r[0] == line_no):
                    results.append((line_no, url, True))
    return results


# ── 检测外部 URL ─

def check_external_url(url: str, session: requests.Session,
                        timeout: int = 8, retry: int = 1):
    """返回 (status_code_or_None, error_msg)"""
    if should_skip(url):
        return (None, "SKIPPED")
    for attempt in range(retry + 1):
        try:
            resp = session.head(url, timeout=timeout, allow_redirects=True, verify=False)
            if resp.status_code < 400:
                return (resp.status_code, "")
            resp = session.get(url, timeout=timeout, allow_redirects=True, stream=True, verify=False)
            resp.close()
            if resp.status_code < 400:
                return (resp.status_code, "")
            return (resp.status_code, f"HTTP {resp.status_code}")
        except Exception as e:
            if attempt < retry:
                time.sleep(0.5)
                continue
            return (None, f"{type(e).__name__}: {e}")
    return (None, "max retries")


# ── 检测内部链接 ─

def check_internal_link(url: str, file_path: Path, docs_dir: Path):
    """检查内部相对路径链接目标是否存在，返回 (exists: bool, resolved_path: str)"""
    try:
        target = (file_path.parent / url).resolve()
        # 安全检查：解析后的路径必须在 docs_dir 内
        docs_dir_resolved = docs_dir.resolve()
        if not str(target).startswith(str(docs_dir_resolved)):
            return (False, f"路径越界: {target}")
        exists = target.exists()
        return (exists, str(target.relative_to(docs_dir_resolved)) if exists else f"不存在: {target}")
    except Exception as e:
        return (False, str(e))


# ── 生成报告 ─

def generate_report(ext_dead, int_dead, docs_dir: Path, output_path: str):
    lines = [
        "# 🔗 死链检测报告",
        "",
        f"- 检测时间：{time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"- 扫描目录：`{docs_dir.resolve()}`",
        f"- ❌ 外部死链：{len(ext_dead)} 条",
        f"- ❌ 内部断链：{len(int_dead)} 条",
        "",
    ]

    if ext_dead:
        lines += [
            "## ❌ 外部死链（HTTP 不可访问）",
            "",
            "| 文件 | 行号 | URL | 状态/错误 |",
            "|------|------|-----|----------|",
        ]
        for rel_path, line_no, url, error in ext_dead:
            lines.append(f"| `{rel_path}` | {line_no} | {url} | {error} |")
        lines += ["", ""]

    if int_dead:
        lines += [
            "## ❌ 内部断链（相对路径目标不存在）",
            "",
            "| 文件 | 行号 | 链接 | 说明 |",
            "|------|------|------|------|",
        ]
        for rel_path, line_no, url, error in int_dead:
            lines.append(f"| `{rel_path}` | {line_no} | `{url}` | {error} |")
        lines += ["", ""]

    if not ext_dead and not int_dead:
        lines += ["## ✅ 未检测到死链或断链！", ""]

    Path(output_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"📝 报告已保存：{output_path}", flush=True)


# ── main ─

def main():
    print("🔍 Infor 生态 - 死链检测脚本启动...", flush=True)

    parser = argparse.ArgumentParser(description="Infor 生态开放资源导航站 - 死链检测")
    parser.add_argument("--docs-dir", default="docs", help="Markdown 目录（默认 docs）")
    parser.add_argument("--timeout", type=int, default=8, help="HTTP 超时秒数（默认 8）")
    parser.add_argument("--retry", type=int, default=1, help="失败重试次数（默认 1）")
    parser.add_argument("--delay", type=float, default=0.2, help="请求间隔秒数（默认 0.2）")
    parser.add_argument("--output", default="dead_links_report.md", help="报告输出路径")
    parser.add_argument("--external-only", action="store_true", help="只检测外部链接")
    args = parser.parse_args()

    docs_dir = Path(args.docs_dir).resolve()
    if not docs_dir.exists():
        print(f"❌ 目录不存在：{docs_dir}", flush=True)
        sys.exit(1)

    print(f"  扫描目录：{docs_dir}", flush=True)

    # 收集链接
    print("🔗 提取链接中...", flush=True)
    md_files = sorted(docs_dir.rglob("*.md"))
    print(f"  找到 {len(md_files)} 个 .md 文件", flush=True)

    all_links = []  # (file_path, line_no, url, is_external)
    for md_file in md_files:
        links = extract_links(md_file)
        for line_no, url, is_ext in links:
            all_links.append((md_file, line_no, url, is_ext))

    ext_links = [l for l in all_links if l[3]]
    int_links = [l for l in all_links if not l[3]]
    print(f"  外部链接：{len(ext_links)} 条，内部链接：{len(int_links)} 条", flush=True)
    print("", flush=True)

    # 检测外部链接
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (compatible; InforEcosystemLinkChecker/1.0)"
    })

    print("🌐 检测外部链接...", flush=True)
    ext_dead = []
    checked = 0
    for fp, line_no, url, _ in ext_links:
        checked += 1
        status, error = check_external_url(url, session, args.timeout, args.retry)
        rel = Path(fp).relative_to(docs_dir)
        if error == "SKIPPED":
            pass  # 静默跳过
        elif status is None or status >= 400:
            ext_dead.append((rel, line_no, url, error))
            print(f"  ❌ [{rel}:{line_no}] {url} → {error}", flush=True)
        if checked % 20 == 0:
            print(f"  进度：{checked}/{len(ext_links)}", flush=True)
        time.sleep(args.delay)
    print(f"  外部链接检测完成，死链：{len(ext_dead)} 条\n", flush=True)

    # 检测内部链接
    int_dead = []
    if not args.external_only:
        print("🔁 检测内部链接...", flush=True)
        for fp, line_no, url, _ in int_links:
            exists, info = check_internal_link(url, fp, docs_dir)
            if not exists:
                rel = Path(fp).relative_to(docs_dir)
                int_dead.append((rel, line_no, url, info))
                print(f"  ❌ [{rel}:{line_no}] `{url}` → {info}", flush=True)
        print(f"  内部链接检测完成，断链：{len(int_dead)} 条\n", flush=True)

    # 生成报告
    generate_report(ext_dead, int_dead, docs_dir, args.output)

    total_dead = len(ext_dead) + len(int_dead)
    if total_dead:
        print(f"❌ 共发现 {total_dead} 条问题链接，请查看报告。", flush=True)
    else:
        print("✅ 所有链接均正常！", flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        print(f"❌ 异常：{e}", flush=True)
        traceback.print_exc()
        sys.exit(1)
