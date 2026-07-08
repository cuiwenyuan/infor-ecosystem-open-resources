#!/usr/bin/env python3
# 品牌名刷新：Coleman AI -> Infor AI（原 Coleman AI），安全版（先 dry-run）
import re, sys
from pathlib import Path

DOCS = Path("docs")
DRY = "--apply" not in sys.argv

# 需要跳过的文件（内部元信息 / 已手动更新，不参与品牌刷新）
SKIP = {"docs/TODO.md", "docs/CHANGELOG.md", "docs/resources/release-notes.md"}

changes = 0

def transform_line(line: str, in_mermaid: bool) -> str:
    global changes
    orig = line
    if in_mermaid:
        # mermaid 节点标签：只改短名称，避免括号破坏图
        line = re.sub(r"Coleman AI", "Infor AI", line)
        line = re.sub(r"(?<![\w（(])Coleman(?![\w）)])", "Infor AI", line)
    else:
        # 1) 平台原名整词
        line = re.sub(r"Coleman AI Platform", "Infor AI Platform（原 Coleman AI Platform）", line)
        # 2) Infor Coleman AI -> Infor AI（原 Coleman AI）
        line = re.sub(r"Infor Coleman AI", "Infor AI（原 Coleman AI）", line)
        # 3) 通用 Coleman AI，带防护（不重复包裹已更新的写法）
        line = re.sub(
            r"(?<!Infor AI \()(?<!Infor AI（)(?<!（原 )(?<!（现 )(?<!Infor )Coleman AI",
            "Infor AI（原 Coleman AI）",
            line,
        )
        # 4) 独立 Coleman（非 Coleman AI 前缀，非已更新上下文）
        line = re.sub(
            r"(?<!Infor AI \()(?<!Infor AI（)(?<!（原 )(?<!（现 )(?<!Infor )(?<![\w（(])Coleman(?![\w）)])",
            "Infor AI（原 Coleman AI）",
            line,
        )
    if line != orig:
        changes += 1
    return line

for fp in sorted(DOCS.rglob("*.md")):
    rel = fp.as_posix()
    if rel in SKIP:
        continue
    lines = fp.read_text(encoding="utf-8").splitlines(keepends=True)
    new_lines = []
    in_mermaid = False
    file_changed = False
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("```mermaid"):
            in_mermaid = True
            new_lines.append(line)
            continue
        if stripped.startswith("```") and in_mermaid:
            in_mermaid = False
            new_lines.append(line)
            continue
        nl = transform_line(line, in_mermaid)
        if nl != line:
            file_changed = True
            if DRY:
                print(f"--- {rel} ---")
                print(f"  - {line.rstrip()}")
                print(f"  + {nl.rstrip()}")
        new_lines.append(nl)
    if file_changed and not DRY:
        fp.write_text("".join(new_lines), encoding="utf-8")

print(f"\n[DRY_RUN={DRY}] 共改动 {changes} 行" + ("" if DRY else "，已写入文件。"))
