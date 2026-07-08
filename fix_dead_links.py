#!/usr/bin/env python3
# 死链修复：精确替换已确认的真实 404 URL（先 dry-run）
import sys
from pathlib import Path

DOCS = Path("docs")
DRY = "--apply" not in sys.argv

# 旧 URL（已确认 404） -> 新 URL（已验证 200）
REPL = {
    "https://www.infor.com/company/legal/": "https://www.infor.com/company/",
    "https://www.infor.com/products/cpq": "https://www.infor.com/products/",
    "https://www.infor.com/products/crm": "https://www.infor.com/products/",
    "https://www.infor.com/company/community": "https://community.infor.com/",
    "https://www.infor.com/products/eam": "https://www.infor.com/products/",
    "https://www.infor.com/customers": "https://www.infor.com/",
    "https://www.infor.cn/customers": "https://www.infor.cn/",
    "https://www.infor.cn/contact": "https://www.infor.cn/",
    "https://www.infor.com/community": "https://community.infor.com/",
    "https://www.infor.com/training": "https://www.infor.com/services/",
    "https://blog.csdn.net/search?q=Infor+ERP": "https://so.csdn.net/so/search?q=Infor",
    "https://blog.csdn.net/search?q=Infor+WMS": "https://so.csdn.net/so/search?q=Infor",
}

hits = 0
for fp in sorted(DOCS.rglob("*.md")):
    text = fp.read_text(encoding="utf-8")
    new = text
    for old, newurl in REPL.items():
        if old in new:
            new = new.replace(old, newurl)
    if new != text:
        hits += 1
        if DRY:
            print(f"--- {fp.as_posix()} ---")
            for old, newurl in REPL.items():
                if old in text:
                    print(f"  {old}  ->  {newurl}")
        else:
            fp.write_text(new, encoding="utf-8")

print(f"\n[DRY_RUN={DRY}] 共改动 {hits} 个文件" + ("" if DRY else "，已写入。"))
