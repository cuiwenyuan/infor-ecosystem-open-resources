# -*- coding: utf-8 -*-
"""
小红书图文 · Infor LN Session 速查页（干货工具贴）
8 张 1080x1440 (3:4) 轮播图，品牌红 #E4002B + 白底
口径：库名 infor-ecosystem-open-resources，不出现 InforIndex，不放二维码
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path(__file__).parent
W, H = 1080, 1440

RED = "#E4002B"
DEEP = "#B80023"
DARK = "#1A1A1A"
GRAY = "#666666"
LIGHT = "#F5F6F8"
GOLD = "#FFD54F"
PALE = "#FFF1F2"
LINE = "#E3E5E8"
BRAND = "infor-ecosystem-open-resources"


def font(size, bold=False):
    name = "msyhbd.ttc" if bold else "msyh.ttc"
    return ImageFont.truetype(f"C:/Windows/Fonts/{name}", size)


f_h1 = font(76, True)      # 主标题
f_h2 = font(56, True)      # 页标题
f_h3 = font(42, True)      # 卡片标题
f_body = font(36)          # 正文
f_small = font(28)         # 小字
f_tiny = font(24)          # 页脚
f_num = font(104, True)    # 大数字
f_num2 = font(72, True)
f_code = font(32, True)


def wrap(text, fnt, maxw, draw):
    """按像素宽度换行（中文逐字，英文优先在空格处断）"""
    lines, cur = [], ""
    for ch in text:
        if draw.textlength(cur + ch, font=fnt) <= maxw:
            cur += ch
        else:
            if " " in cur and ch != " ":
                i = cur.rfind(" ")
                lines.append(cur[:i])
                cur = cur[i + 1:] + ch
            else:
                lines.append(cur)
                cur = ch
    if cur:
        lines.append(cur)
    return lines


def text(draw, xy, s, fnt, fill=DARK, maxw=None, spacing=1.35):
    x, y = xy
    lines = wrap(s, fnt, maxw, draw) if maxw else [s]
    lh = int(fnt.size * spacing)
    for ln in lines:
        draw.text((x, y), ln, fill=fill, font=fnt)
        y += lh
    return y


def header(img, draw, idx, title, subtitle=None, accent=RED):
    """白底通用页头 + 页码 + 页脚"""
    draw.rectangle([0, 0, W, 14], fill=accent)
    draw.rounded_rectangle([64, 62, 92, 90], radius=8, fill=accent)
    text(draw, (108, 58), "LN SESSION 速查", font(30, True), GRAY)
    draw.text((W - 64 - draw.textlength(f"{idx:02d}/08", font=font(30, True)), 58),
              f"{idx:02d}/08", fill=GRAY, font=font(30, True))
    y = 128
    y = text(draw, (64, y), title, f_h2, DARK, W - 128)
    if subtitle:
        y = text(draw, (64, y + 16), subtitle, f_body, GRAY, W - 128)
    draw.line([64, H - 92, W - 64, H - 92], fill=LINE, width=2)
    draw.text((64, H - 74), BRAND, fill=GRAY, font=f_tiny)
    draw.text((W - 64 - draw.textlength("开源免费 · 持续更新", font=f_tiny), H - 74),
              "开源免费 · 持续更新", fill=GRAY, font=f_tiny)
    return y + 40


def magnifier(draw, x, y, color=RED, r=15):
    """画一个放大镜（圆 + 柄），避免字体不含 emoji"""
    draw.ellipse([x - r, y - r, x + r, y + r], outline=color, width=4)
    draw.line([x + r - 2, y + r - 2, x + r + 12, y + r + 12], fill=color, width=5)


def caret(draw, x, y, color=GRAY, s=11):
    """画下拉三角，避免字体缺字变豆腐块"""
    draw.polygon([(x, y), (x + 2 * s, y), (x + s, y + s)], fill=color)


def card(draw, box, title, body, accent=RED, fill=LIGHT):
    draw.rounded_rectangle(box, radius=24, fill=fill)
    x1, y1, x2, y2 = box
    draw.rounded_rectangle([x1 + 28, y1 + 34, x1 + 36, y1 + 82], radius=4, fill=accent)
    text(draw, (x1 + 56, y1 + 28), title, f_h3, DARK, x2 - x1 - 90)
    text(draw, (x1 + 56, y1 + 100), body, f_body, GRAY, x2 - x1 - 90)


# ---------------- 01 封面 ----------------
img = Image.new("RGB", (W, H), DEEP)
d = ImageDraw.Draw(img)
for x in range(W):
    t = x / W
    d.line([(x, 0), (x, H)], fill=(int(0xA8 + 0x3C * t), 0, int(0x1B + 0x10 * t)))
# 装饰圆
d.ellipse([W - 320, H - 420, W + 140, H + 40], outline="#FFFFFF", width=2)
d.ellipse([W - 220, -160, W + 200, 260], outline="#FFFFFF", width=2)

d.rounded_rectangle([64, 68, 520, 116], radius=24, fill="#FFFFFF")
d.text((88, 76), "INFOR LN · 顾问 / 4GL 开发收藏", fill=DEEP, font=font(26, True))

y = 176
y = text(d, (64, y), "查 LN Session", f_h1, "#FFFFFF", W - 128)
y = text(d, (64, y + 8), "别再翻官方文档了", f_h1, "#FFFFFF", W - 128)
d.text((64, y + 34), "12,125 条 · 中英双语 · 一搜就有", fill=GOLD, font=font(48, True))

# 模拟搜索框
sb = [64, 620, W - 64, 726]
d.rounded_rectangle(sb, radius=28, fill="#FFFFFF")
magnifier(d, 116, 673, GRAY, 16)
d.text((158, 650), "tdsls4100m000", fill=DARK, font=font(40, True))
d.rounded_rectangle([W - 250, 638, W - 96, 708], radius=20, fill=RED)
d.text((W - 226, 650), "即搜即达", fill="#FFFFFF", font=font(28, True))

# 数据 pills
pills = ["23 个包", "208 模块组", "五版本官方链接", "开源免费"]
px, py = 64, 790
for p in pills:
    w = d.textlength(p, font=font(28, True))
    d.rounded_rectangle([px - 12, py - 8, px + w + 12, py + 46], radius=26,
                        outline="#FFFFFF", width=2)
    d.text((px, py), p, fill="#FFFFFF", font=font(28, True))
    px += w + 40
    if px > W - 200:
        px, py = 64, py + 76

d.line([64, H - 180, W - 64, H - 180], fill="#FFFFFF", width=2)
d.text((64, H - 150), BRAND, fill="#FFFFFF", font=font(26, True))
d.text((64, H - 108), "Infor 生态开放资源导航 · 非官方 · 免费开源", fill="#FFD8DD", font=font(26))
img.save(OUT / "01-cover.png")

# ---------------- 02 痛点 ----------------
img = Image.new("RGB", (W, H), "#FFFFFF")
d = ImageDraw.Draw(img)
y = header(img, d, 2, "是不是每天都在找 Session？", "做 LN 的都懂，官方文档权威，但查找路径太深了")
card(d, [64, y, W - 64, y + 250], "配个参数",
     "维护物料主数据的 session，是 tiitm0101m000 还是 tiitm0107m000？")
card(d, [64, y + 274, W - 64, y + 524], "客户现场",
     "报错了要快速定位功能入口，网络还受限，翻文档树翻到怀疑人生")
card(d, [64, y + 548, W - 64, y + 798], "写 4GL 定制",
     "要查标准 session 的编号和用途，中文资料零散，搜半天搜不到")
d.rounded_rectangle([64, y + 830, W - 64, y + 936], radius=24, fill=PALE)
d.text((96, y + 862), "痛点不是没有资料，是「输入关键字马上找到」的地方一直没有",
       fill=DEEP, font=font(32, True))
img.save(OUT / "02-pain.png")

# ---------------- 03 数据大字报 ----------------
img = Image.new("RGB", (W, H), "#FFFFFF")
d = ImageDraw.Draw(img)
y = header(img, d, 3, "我们把官方 Session 全收齐了", "合并官方 Sitemap 全量 + 10.7 中文联机帮助采集")
blocks = [
    ("12,125", "条 Session"), ("23", "个包"),
    ("208", "个模块组"), ("10,626", "条中文描述"),
]
for i, (n, lab) in enumerate(blocks):
    cx = 64 + (i % 2) * ((W - 128) // 2 + 8)
    cy = y + (i // 2) * 290
    bw, bh = (W - 128) // 2 - 8, 264
    d.rounded_rectangle([cx, cy, cx + bw, cy + bh], radius=24, fill=LIGHT)
    d.rectangle([cx, cy, cx + 8, cy + bh], fill=RED)
    f = f_num if len(n) <= 5 else f_num2
    d.text((cx + 36, cy + 44), n, fill=RED, font=f)
    d.text((cx + 38, cy + 176), lab, fill=GRAY, font=f_body)
d.rounded_rectangle([64, y + 600, W - 64, y + 710], radius=24, fill=PALE)
d.text((96, y + 636), "数据源：docs.infor.com 官方 Sitemap + 联机帮助 · 2026-11 更新",
       fill=DEEP, font=font(30, True))
img.save(OUT / "03-numbers.png")

# ---------------- 04 包分布 ----------------
img = Image.new("RGB", (W, H), "#FFFFFF")
d = ImageDraw.Draw(img)
y = header(img, d, 4, "覆盖哪些包？", "条数 Top 8（共 23 个包）")
rows = [
    ("tf", "财务", 1766), ("tc", "通用", 1654), ("td", "分销", 1342),
    ("ti", "制造", 1299), ("ts", "企业服务", 1072), ("tp", "项目", 999),
    ("wh", "仓储", 937), ("pd", "产品开发", 516),
]
bar_x, bar_w = 300, W - 300 - 190
for i, (pkg, label, n) in enumerate(rows):
    by = y + i * 112
    d.text((64, by + 6), pkg.upper(), fill=DARK, font=f_code)
    d.text((150, by + 8), label, fill=GRAY, font=f_small)
    d.rounded_rectangle([bar_x, by + 12, bar_x + bar_w, by + 52], radius=14, fill=LIGHT)
    d.rounded_rectangle([bar_x, by + 12, bar_x + int(bar_w * n / 1766), by + 52],
                        radius=14, fill=RED)
    d.text((W - 175, by + 6), f"{n:,}", fill=DARK, font=font(34, True))
d.line([64, y + 930, W - 64, y + 930], fill=LINE, width=2)
d.text((64, y + 958), "其他 15 包 2,540 条：本地化 / 质量 / EDI / 货运 / 工具 / 迁移…",
       fill=GRAY, font=f_small)
img.save(OUT / "04-packages.png")

# ---------------- 05 搜索演示 ----------------
img = Image.new("RGB", (W, H), "#FFFFFF")
d = ImageDraw.Draw(img)
y = header(img, d, 5, "输入什么都能搜", "Code / 中文 / 英文，表格即时过滤")
sb = [64, y, W - 64, y + 110]
d.rounded_rectangle(sb, radius=26, fill=LIGHT, outline=RED, width=3)
magnifier(d, 116, y + 55, RED, 16)
d.text((158, y + 32), "tdsls4100", fill=DARK, font=font(44, True))
d.rounded_rectangle([W - 250, y + 18, W - 92, y + 92], radius=20, fill=RED)
d.text((W - 224, y + 38), "搜索", fill="#FFFFFF", font=font(30, True))

chips = ["Session Code  tdsls4100m000", "中文  销售订单", "英文  purchase"]
cx = 64
for c in chips:
    w = d.textlength(c, font=font(28))
    d.rounded_rectangle([cx - 10, y + 140, cx + w + 10, y + 196], radius=28, fill=PALE)
    d.text((cx, y + 152), c, fill=DEEP, font=font(28))
    cx += w + 40

# 结果表格
ty = y + 250
d.rounded_rectangle([64, ty, W - 64, ty + 62], radius=10, fill=RED)
for x, t in [(86, "Session Code"), (420, "中文描述"), (760, "包/模块")]:
    d.text((x, ty + 14), t, fill="#FFFFFF", font=font(28, True))
data = [
    ("tdsls4100m000", "销售订单", "td/sls"),
    ("tdsls4101m000", "销售订单行", "td/sls"),
    ("tdpur4000m000", "采购订单", "td/pur"),
    ("tfgld1101m000", "事务处理", "tf/gld"),
]
for i, (a, b, c) in enumerate(data):
    ry = ty + 62 + i * 72
    if i % 2 == 0:
        d.rectangle([64, ry, W - 64, ry + 72], fill=LIGHT)
    d.text((86, ry + 18), a, fill=DARK, font=font(28, True))
    d.text((420, ry + 18), b, fill=DARK, font=font(28))
    d.text((760, ry + 18), c, fill=GRAY, font=font(28))
d.text((64, ty + 372), "▲ 不用跳转、不用等页面，本页即时过滤", fill=DEEP, font=font(30, True))
img.save(OUT / "05-search.png")

# ---------------- 06 筛选 + 表格 ----------------
img = Image.new("RGB", (W, H), "#FFFFFF")
d = ImageDraw.Draw(img)
y = header(img, d, 6, "还能按包 / 模块筛", "两级联动，只看该模块的 Session")
# 下拉示意
d.rounded_rectangle([64, y, 490, y + 96], radius=20, fill=LIGHT, outline=LINE, width=2)
d.text((94, y + 26), "包：tf  财务管理", fill=DARK, font=font(32, True))
caret(d, 432, y + 38)
d.rounded_rectangle([520, y, W - 64, y + 96], radius=20, fill=LIGHT, outline=LINE, width=2)
d.text((550, y + 26), "模块：gld  总帐", fill=DARK, font=font(32, True))
caret(d, W - 108, y + 38)
# 紧凑表格
ty = y + 140
d.rounded_rectangle([64, ty, W - 64, ty + 58], radius=10, fill=RED)
for x, t in [(80, "Session Code"), (350, "中文"), (620, "EN"), (860, "官方")]:
    d.text((x, ty + 12), t, fill="#FFFFFF", font=font(26, True))
data = [
    ("tfgld1101m000", "事务处理", "Transactions", "↗"),
    ("tfgld1102m000", "事务处理类型", "Transaction Types", "↗"),
    ("tfgld1103m000", "总帐参数", "GL Parameters", "↗"),
    ("tfgld1104m000", "会计科目", "Chart of Accounts", "↗"),
    ("tfgld1105m000", "期间", "Periods", "↗"),
]
for i, row in enumerate(data):
    ry = ty + 58 + i * 66
    if i % 2 == 0:
        d.rectangle([64, ry, W - 64, ry + 66], fill=LIGHT)
    for x, t, f in [(80, row[0], font(26, True)), (350, row[1], font(26)),
                    (620, row[2], font(24)), (880, row[3], font(28, True))]:
        d.text((x, ry + 16), t, fill=DARK if f.size >= 26 else GRAY, font=f)
d.rounded_rectangle([64, ty + 420, W - 64, ty + 524], radius=24, fill=PALE)
d.text((96, ty + 452), "按包分片懒加载，首屏轻快，手机上也不卡", fill=DEEP, font=font(30, True))
img.save(OUT / "06-filter.png")

# ---------------- 07 五版本 ----------------
img = Image.new("RGB", (W, H), "#FFFFFF")
d = ImageDraw.Draw(img)
y = header(img, d, 7, "一个页面，五个官方文档版本", "工具栏切换「官方」列的链接目标")
vers = [
    ("10.7 zh-cn", "主口径 · 中文"), ("10.6 zh-cn", "10.7 已验证集"),
    ("10.8 zh-cn", "分册结构"), ("2024.x Cloud zh-cn", "中文可用"),
    ("2025.x Cloud en-us", "官方仅英文"),
]
for i, (v, note) in enumerate(vers):
    cy = y + i * 128
    fill = RED if i == 0 else LIGHT
    d.rounded_rectangle([64, cy, W - 64, cy + 104], radius=20, fill=fill)
    d.text((96, cy + 22), v, fill="#FFFFFF" if i == 0 else DARK, font=font(38, True))
    d.text((W - 64 - d.textlength(note, font=font(28)), cy + 34), note,
           fill="#FFD8DD" if i == 0 else GRAY, font=font(28))
d.line([64, y + 670, W - 64, y + 670], fill=LINE, width=2)
text(d, (64, y + 700), "每条按官方 Sitemap 严格标注可用版本，该版本没收录就显示「—」，不给你死链。",
     font(32, True), DEEP, W - 128)
text(d, (64, y + 800), "10.5 官方文档库不完整（部分包缺失、无 Sitemap），只提供文档库入口检索。",
     f_small, GRAY, W - 128)
img.save(OUT / "07-versions.png")

# ---------------- 08 收尾 ----------------
img = Image.new("RGB", (W, H), "#FFFFFF")
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 14], fill=RED)
d.rounded_rectangle([64, 62, 92, 90], radius=8, fill=RED)
text(d, (108, 58), "LN SESSION 速查", font(30, True), GRAY)
d.text((W - 64 - d.textlength("08/08", font=font(30, True)), 58), "08/08",
       fill=GRAY, font=font(30, True))

y = 150
y = text(d, (64, y), "免费 · 开源", f_h1, DARK, W - 128)
y = text(d, (64, y + 8), "持续更新", f_h1, RED, W - 128)

d.rounded_rectangle([64, 420, W - 64, 540], radius=24, fill=LIGHT)
d.text((94, 452), BRAND, fill=DEEP, font=font(38, True))
d.text((94, 502), "Infor 生态开放资源导航 · 非官方", fill=GRAY, font=f_small)

d.text((64, 590), "页面地址", fill=GRAY, font=f_small)
d.rounded_rectangle([64, 630, W - 64, 730], radius=20, fill=PALE)
d.text((88, 646), "cuiwenyuan.github.io/infor-ecosystem-open-resources/",
       fill=DEEP, font=font(26, True))
d.text((88, 684), "resources/ln-sessions/", fill=DEEP, font=font(26, True))

d.rounded_rectangle([64, 780, W - 64, 900], radius=24, fill=RED)
text(d, (96, 806), "主页简介 / 评论区 / 搜库名，都能找到", font(36, True), "#FFFFFF", W - 192)

d.text((64, 950), "收藏这一篇，下次查 Session 不用慌", fill=DARK, font=font(38, True))
d.text((64, 1030), "你最常用的 Session 是哪个？评论区聊聊", fill=GRAY, font=f_body)
d.text((64, 1100), "转发给身边做 Infor LN 的同事和朋友", fill=GRAY, font=f_body)

d.line([64, H - 92, W - 64, H - 92], fill=LINE, width=2)
d.text((64, H - 74), BRAND, fill=GRAY, font=f_tiny)
d.text((W - 64 - d.textlength("开源免费 · 持续更新", font=f_tiny), H - 74),
       "开源免费 · 持续更新", fill=GRAY, font=f_tiny)
img.save(OUT / "08-cta.png")

print("saved 8 images:", [p.name for p in sorted(OUT.glob("0*.png"))])
