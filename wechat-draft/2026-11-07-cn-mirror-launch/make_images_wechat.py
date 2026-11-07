# -*- coding: utf-8 -*-
"""
微信贴图（公众号图片消息 / 小绿书）· 国内镜像站正式上线
9 张 1080x1440 (3:4) 横滑图，品牌红 #E4002B + 白底
口径：对外统一使用库名 infor-ecosystem-open-resources，不使用任何旧站名简称
视觉：沿用 2026-11-05 LN Session 微信贴图版（同字体 / 同色板 / 同版式）
第 9 张二维码指向国内站首页，微信内长按识别直达
数据：2026-11-07 同一网络 curl 实测，首页国内 0.098/0.100/0.104s，
      GitHub Pages 0.904/1.540/7.064s；sitemap 178 条全为 .cn
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
WHITE = "#FFFFFF"
BRAND = "infor-ecosystem-open-resources"
DOMAIN = "infor-ecosystem-open-resources.cuiwenyuan.cn"
URL = "https://infor-ecosystem-open-resources.cuiwenyuan.cn/"
SECTION = "国内镜像站上线"


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


def center(draw, y, s, fnt, fill=DARK):
    draw.text(((W - draw.textlength(s, font=fnt)) / 2, y), s, fill=fill, font=fnt)


def header(img, draw, idx, title, subtitle=None, accent=RED):
    """白底通用页头 + 页码 + 页脚"""
    draw.rectangle([0, 0, W, 14], fill=accent)
    draw.rounded_rectangle([64, 62, 92, 90], radius=8, fill=accent)
    text(draw, (108, 58), SECTION, font(30, True), GRAY)
    draw.text((W - 64 - draw.textlength(f"{idx:02d}/09", font=font(30, True)), 58),
              f"{idx:02d}/09", fill=GRAY, font=font(30, True))
    y = 128
    y = text(draw, (64, y), title, f_h2, DARK, W - 128)
    if subtitle:
        y = text(draw, (64, y + 16), subtitle, f_body, GRAY, W - 128)
    draw.line([64, H - 92, W - 64, H - 92], fill=LINE, width=2)
    draw.text((64, H - 74), BRAND, fill=GRAY, font=f_tiny)
    draw.text((W - 64 - draw.textlength("开源免费 · 持续更新", font=f_tiny), H - 74),
              "开源免费 · 持续更新", fill=GRAY, font=f_tiny)
    return y + 40


def footer(draw, accent=RED):
    draw.rectangle([0, 0, W, 14], fill=accent)
    draw.rounded_rectangle([64, 62, 92, 90], radius=8, fill=accent)
    text(draw, (108, 58), SECTION, font(30, True), GRAY)
    draw.line([64, H - 92, W - 64, H - 92], fill=LINE, width=2)
    draw.text((64, H - 74), BRAND, fill=GRAY, font=f_tiny)
    draw.text((W - 64 - draw.textlength("开源免费 · 持续更新", font=f_tiny), H - 74),
              "开源免费 · 持续更新", fill=GRAY, font=f_tiny)


def card(draw, box, title, body, accent=RED, fill=LIGHT):
    draw.rounded_rectangle(box, radius=24, fill=fill)
    x1, y1, x2, y2 = box
    draw.rounded_rectangle([x1 + 28, y1 + 34, x1 + 36, y1 + 82], radius=4, fill=accent)
    text(draw, (x1 + 56, y1 + 28), title, f_h3, DARK, x2 - x1 - 90)
    text(draw, (x1 + 56, y1 + 104), body, f_body, GRAY, x2 - x1 - 90)


def check(draw, x, y, size=36, color=RED):
    """几何对勾（圆底 + 白勾），避免字体缺字变豆腐块"""
    draw.ellipse([x, y, x + size, y + size], fill=color)
    draw.line([(x + 9, y + 18), (x + 15, y + 25), (x + 27, y + 11)],
              fill=WHITE, width=4, joint="curve")


def arrow_down(draw, x, y1, y2, color=RED, width=5):
    draw.line([(x, y1), (x, y2 - 14)], fill=color, width=width)
    draw.polygon([(x - 11, y2 - 14), (x + 11, y2 - 14), (x, y2)], fill=color)


def globe(draw, x, y, r=16, color=GRAY):
    """画一个地球仪小图标（圆 + 经纬线），避免 emoji"""
    draw.ellipse([x - r, y - r, x + r, y + r], outline=color, width=3)
    draw.line([x - r, y, x + r, y], fill=color, width=2)
    draw.ellipse([x - r // 2, y - r, x + r // 2, y + r], outline=color, width=2)


# ---------------- 01 封面 ----------------
img = Image.new("RGB", (W, H), DEEP)
d = ImageDraw.Draw(img)
for x in range(W):
    t = x / W
    d.line([(x, 0), (x, H)], fill=(int(0xA8 + 0x3C * t), 0, int(0x1B + 0x10 * t)))
d.ellipse([W - 320, H - 420, W + 140, H + 40], outline=WHITE, width=2)
d.ellipse([W - 220, -160, W + 200, 260], outline=WHITE, width=2)

d.rounded_rectangle([64, 68, 590, 116], radius=24, fill=WHITE)
d.text((88, 76), "INFOR 生态 · 国内访问提速", fill=DEEP, font=font(26, True))

y = 176
y = text(d, (64, y), "GitHub 站打开慢？", f_h1, WHITE, W - 128)
y = text(d, (64, y + 8), "国内镜像已上线", f_h1, WHITE, W - 128)
d.text((64, y + 34), "首页实测 0.10s · 免费开源", fill=GOLD, font=font(44, True))

# 模拟浏览器地址栏
sb = [64, 620, W - 64, 726]
d.rounded_rectangle(sb, radius=28, fill=WHITE)
globe(d, 116, 673, 16, GRAY)
d.text((152, 652), DOMAIN, fill=DARK, font=font(26, True))
d.rounded_rectangle([W - 250, 638, W - 96, 708], radius=20, fill=RED)
d.text((W - 222, 650), "秒开", fill=WHITE, font=font(30, True))

pills = ["首页 0.10s", "178 页同步", "零境外请求", "自动更新"]
px, py = 64, 790
for p in pills:
    w = d.textlength(p, font=font(28, True))
    d.rounded_rectangle([px - 12, py - 8, px + w + 12, py + 46], radius=26,
                        outline=WHITE, width=2)
    d.text((px, py), p, fill=WHITE, font=font(28, True))
    px += w + 32
    if px > W - 200:
        px, py = 64, py + 76

d.line([64, H - 180, W - 64, H - 180], fill=WHITE, width=2)
d.text((64, H - 150), BRAND, fill=WHITE, font=font(26, True))
d.text((64, H - 108), "Infor 生态开放资源导航 · 非官方 · 免费开源", fill="#FFD8DD", font=font(26))
img.save(OUT / "01-cover.png")

# ---------------- 02 痛点 ----------------
img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)
y = header(img, d, 2, "GitHub 站，国内打开是真的慢", "不是内容不好，是加载这一步太折腾")
card(d, [64, y, W - 64, y + 250], "页面转圈",
     "查一条 Session，首页转五六秒才出来，急着用的时候最难受")
card(d, [64, y + 274, W - 64, y + 524], "字体加载不出来",
     "字体走 Google Fonts，国内常被卡住，排版还会跳一下")
card(d, [64, y + 548, W - 64, y + 798], "偶尔直接超时",
     "客户现场网络限制多，境外站点有时干脆打不开")
d.rounded_rectangle([64, y + 830, W - 64, y + 936], radius=24, fill=PALE)
d.text((96, y + 862), "痛点不是没资源，是「国内打开」这一步一直不稳",
       fill=DEEP, font=font(32, True))
img.save(OUT / "02-pain.png")

# ---------------- 03 实测数据 ----------------
img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)
y = header(img, d, 3, "实测：快了多少？", "2026-11-07 同一网络，首页各测 3 次")
blocks = [
    ("0.10s", "国内镜像 · 3 次均值"),
    ("7.06s", "GitHub Pages · 最慢一次"),
    ("0.90s", "GitHub Pages · 最快一次"),
    ("178", "sitemap 全量页面"),
]
for i, (n, lab) in enumerate(blocks):
    cx = 64 + (i % 2) * ((W - 128) // 2 + 8)
    cy = y + (i // 2) * 290
    bw, bh = (W - 128) // 2 - 8, 264
    d.rounded_rectangle([cx, cy, cx + bw, cy + bh], radius=24, fill=LIGHT)
    d.rectangle([cx, cy, cx + 8, cy + bh], fill=RED)
    f = f_num if len(n) <= 3 else f_num2
    d.text((cx + 36, cy + 44), n, fill=RED, font=f)
    d.text((cx + 38, cy + 176), lab, fill=GRAY, font=font(28))

# 速度对比条
by = y + 600
d.text((64, by), "首页耗时对比", fill=DARK, font=font(32, True))
bar_x, bar_w = 300, W - 300 - 240
for i, (label, val, ratio, color) in enumerate([
    ("国内镜像", "0.10s", 0.10 / 7.06, RED),
    ("GitHub 均值", "3.17s", 3.17 / 7.06, "#B0B4BB"),
    ("GitHub 最慢", "7.06s", 1.0, "#D8DBE0"),
]):
    ry = by + 60 + i * 88
    d.text((64, ry + 10), label, fill=GRAY, font=font(28))
    d.rounded_rectangle([bar_x, ry + 8, bar_x + bar_w, ry + 52], radius=14, fill=LIGHT)
    d.rounded_rectangle([bar_x, ry + 8, bar_x + max(24, int(bar_w * ratio)), ry + 52],
                        radius=14, fill=color)
    d.text((bar_x + bar_w + 20, ry + 10), val, fill=DARK, font=font(28, True))

d.rounded_rectangle([64, y + 920, W - 64, y + 1020], radius=24, fill=PALE)
d.text((96, y + 952), "同一时刻 curl 实测，条越短越快 · 数值仅供参考",
       fill=DEEP, font=font(30, True))
img.save(OUT / "03-numbers.png")

# ---------------- 04 双站架构 ----------------
img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)
y = header(img, d, 4, "一次推送，两个站点同时更新", "GitHub Actions 两个并行 job，失败互不影响")

d.rounded_rectangle([64, y, W - 64, y + 110], radius=24, fill=RED)
center(d, y + 28, "git push main", font(44, True), WHITE)
arrow_down(d, W // 2, y + 110, y + 176)

d.rounded_rectangle([64, y + 176, W - 64, y + 300], radius=24, fill=LIGHT)
center(d, y + 202, "GitHub Actions · 双 job 并行", font(38, True), DARK)
center(d, y + 254, "同一次触发，互不依赖", font(26), GRAY)

cx, lx, rx = W // 2, 292, W - 292
d.line([(cx, y + 300), (cx, y + 344)], fill=RED, width=5)
d.line([(lx, y + 344), (rx, y + 344)], fill=RED, width=5)
arrow_down(d, lx, y + 344, y + 400)
arrow_down(d, rx, y + 344, y + 400)

for bx, name, sub, lines in [
    (64, "deploy", "GitHub Pages 站", ["mkdocs.yml 零改动", "Google Fonts 原样", "全球访问"]),
    (560, "deploy-cn", "国内镜像站", ["mkdocs.cn.yml", "FTP 增量同步", "国内节点"]),
]:
    d.rounded_rectangle([bx, y + 400, bx + 456, y + 650], radius=24,
                        fill=WHITE, outline=RED, width=3)
    d.text((bx + 32, y + 424), name, fill=RED, font=font(38, True))
    d.text((bx + 32, y + 482), sub, fill=DARK, font=font(32, True))
    for k, ln in enumerate(lines):
        d.text((bx + 32, y + 534 + k * 32), "· " + ln, fill=GRAY, font=font(24))

d.rounded_rectangle([64, y + 680, W - 64, y + 800], radius=24, fill=PALE)
d.text((96, y + 706), "内容同一份，元数据各自生成", fill=DEEP, font=font(34, True))
d.text((96, y + 754), "两站 site_url 不同，canonical / sitemap / JSON-LD 分开写",
       fill=GRAY, font=font(26))

d.rounded_rectangle([64, y + 830, W - 64, y + 950], radius=24, fill=LIGHT)
text(d, (96, y + 860), "否则搜索引擎会把国内站判成 GitHub Pages 的重复内容。实测 sitemap.xml 178 条全为 .cn 域名、0 条 github.io。",
     font(28), GRAY, W - 192)
img.save(OUT / "04-architecture.png")

# ---------------- 05 两站差异表 ----------------
img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)
y = header(img, d, 5, "两站有什么不一样？", "内容完全相同，只有前端资源与元数据不同")
cols = [64, 268, 648, W - 64]
ty = y
d.rounded_rectangle([64, ty, W - 64, ty + 64], radius=10, fill=RED)
for i, t in enumerate(["项目", "GitHub Pages 站", "国内镜像站"]):
    d.text((cols[i] + 18, ty + 16), t, fill=WHITE, font=font(28, True))
rows = [
    ("地址", "github.io 子路径", ".cn 根域名"),
    ("字体", "Google Fonts", "自托管 woff2"),
    ("图表", "unpkg mermaid", "本地 mermaid.min.js"),
    ("境外请求", "有", "0"),
    ("元数据", "github.io canonical", ".cn canonical / sitemap"),
    ("外观", "原样", "视觉一致"),
]
for i, row in enumerate(rows):
    ry = ty + 64 + i * 122
    if i % 2 == 0:
        d.rectangle([64, ry, W - 64, ry + 122], fill=LIGHT)
    for j, cell in enumerate(row):
        f = font(28, True) if j == 0 else font(26)
        fill = DARK if j == 0 else (RED if j == 2 and cell in ("0", ".cn 根域名") else GRAY)
        text(d, (cols[j] + 18, ry + 22), cell, f, fill, cols[j + 1] - cols[j] - 32)
    d.line([64, ry + 122, W - 64, ry + 122], fill=LINE, width=2)

d.rounded_rectangle([64, y + 830, W - 64, y + 940], radius=24, fill=PALE)
d.text((96, y + 862), "主 mkdocs.yml 一个字没改，老站外观完全不变",
       fill=DEEP, font=font(30, True))
img.save(OUT / "05-compare.png")

# ---------------- 06 三项优化 ----------------
img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)
y = header(img, d, 6, "不只是搬了个服务器", "国内站专门做了三件事，页面零境外前端请求")
card(d, [64, y, W - 64, y + 250], "字体自托管",
     "Roboto / Roboto Mono 的 woff2 放本地，同名 @font-face 复刻 Google Fonts 视觉")
card(d, [64, y + 274, W - 64, y + 524], "图表本地化",
     "Mermaid 3.3 MB 放进站点，不再向 unpkg.com 发请求，弱网也能看图")
card(d, [64, y + 548, W - 64, y + 798], "独立元数据",
     "独立 site_url，canonical / sitemap.xml / JSON-LD 全按 .cn 域名生成")
d.rounded_rectangle([64, y + 830, W - 64, y + 936], radius=24, fill=PALE)
d.text((96, y + 862), "实测页面源码：googleapis / gstatic / unpkg 均为 0",
       fill=DEEP, font=font(30, True))
img.save(OUT / "06-optimize.png")

# ---------------- 07 验收清单 ----------------
img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)
y = header(img, d, 7, "上线前，逐项实测过", "不只看 Actions 变绿，还要真的打开看")
items = [
    "首页 HTTP 200，HTTPS / HSTS 正常",
    "woff2 字体、本地 mermaid 全部 200",
    "零 googleapis / gstatic / unpkg 请求",
    "canonical 指向 .cn 域名",
    "sitemap 178 条全为 .cn，0 条 github.io",
    "LN Session 分片 JSON、二维码图均可访问",
    "GitHub 站外观零改动，Google Fonts 保留",
]
for i, it in enumerate(items):
    ry = y + i * 118
    if i % 2 == 0:
        d.rounded_rectangle([64, ry, W - 64, ry + 106], radius=18, fill=LIGHT)
    check(d, 92, ry + 35)
    text(d, (152, ry + 24), it, font(30, True), DARK, W - 220)

d.rounded_rectangle([64, y + 860, W - 64, y + 960], radius=24, fill=PALE)
d.text((96, y + 892), "2026-11-07 全项通过，实测数据已记入 DEPLOY.md",
       fill=DEEP, font=font(30, True))
img.save(OUT / "07-checklist.png")

# ---------------- 08 收尾 ----------------
img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)
footer(d)
d.text((W - 64 - d.textlength("08/09", font=font(30, True)), 58), "08/09",
       fill=GRAY, font=font(30, True))

y = 150
y = text(d, (64, y), "免费 · 开源", f_h1, DARK, W - 128)
y = text(d, (64, y + 8), "国内也能秒开", f_h1, RED, W - 128)

d.rounded_rectangle([64, 420, W - 64, 540], radius=24, fill=LIGHT)
d.text((94, 452), BRAND, fill=DEEP, font=font(38, True))
d.text((94, 502), "Infor 生态开放资源导航 · 非官方", fill=GRAY, font=f_small)

d.text((64, 590), "国内站地址", fill=GRAY, font=f_small)
d.rounded_rectangle([64, 630, W - 64, 730], radius=20, fill=PALE)
d.text((88, 646), "infor-ecosystem-open-resources", fill=DEEP, font=font(30, True))
d.text((88, 686), ".cuiwenyuan.cn", fill=DEEP, font=font(30, True))

d.rounded_rectangle([64, 780, W - 64, 900], radius=24, fill=RED)
text(d, (96, 806), "下一页可扫码 · 搜库名也能找到", font(36, True), WHITE, W - 192)

d.text((64, 950), "收藏这一篇，下次国内访问不用愁", fill=DARK, font=font(38, True))
d.text((64, 1030), "你平时用哪个站？评论区聊聊", fill=GRAY, font=f_body)
d.text((64, 1100), "点个「在看」，转发给做 Infor 的同事", fill=GRAY, font=f_body)
img.save(OUT / "08-cta.png")

# ---------------- 09 二维码直达 ----------------
import qrcode

_qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=12, border=4)
_qr.add_data(URL)
_qr.make(fit=True)
_qr.make_image(fill_color="black", back_color="white").save(OUT / "qrcode-plain.png")
_qim = Image.open(OUT / "qrcode-plain.png").convert("RGB")

img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)
footer(d)
d.text((W - 64 - d.textlength("09/09", font=font(30, True)), 58), "09/09",
       fill=GRAY, font=font(30, True))

y = 150
y = text(d, (64, y), "扫码直达", f_h1, DARK, W - 128)
y = text(d, (64, y + 8), "国内秒开", f_h1, RED, W - 128)

QS = 600
QX, QY = (W - QS) // 2, 430
d.rounded_rectangle([QX - 30, QY - 30, QX + QS + 30, QY + QS + 30],
                    radius=28, fill=WHITE, outline=LINE, width=3)
img.paste(_qim.resize((QS, QS), Image.LANCZOS), (QX, QY))

d.rounded_rectangle([64, 1090, W - 64, 1184], radius=24, fill=PALE)
_hint = "微信长按识别二维码 · 一键直达国内站"
d.text(((W - d.textlength(_hint, font=font(32, True))) / 2, 1120), _hint,
       fill=DEEP, font=font(32, True))

_u1 = "infor-ecosystem-open-resources"
_u2 = ".cuiwenyuan.cn"
for _yy, _u in [(1214, _u1), (1252, _u2)]:
    d.text(((W - d.textlength(_u, font=font(26))) / 2, _yy), _u,
           fill=GRAY, font=font(26))
img.save(OUT / "09-qrcode.png")

print("saved 9 images:", [p.name for p in sorted(OUT.glob("0*.png"))])
