# -*- coding: utf-8 -*-
"""
小红书 / 微信小绿书图文 · 2026 Infor 中国区新客户与新项目
9 张 1080x1440 (3:4)，品牌红 #E4002B + 白底，沿用 2026-11-05 那套视觉
口径：库名 infor-ecosystem-open-resources，不出现 InforIndex
第 9 张为专题页二维码（微信内可用，小红书发布时可只传 01-08）
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import qrcode

OUT = Path(__file__).parent
W, H = 1080, 1440
FOOT = H - 92
SAFE = W - 64

RED = "#E4002B"
DEEP = "#B80023"
DARK = "#1A1A1A"
GRAY = "#666666"
LIGHT = "#F5F6F8"
PALE = "#FFF1F2"
LINE = "#E3E5E8"
GOLD = "#FFD54F"
BRAND = "infor-ecosystem-open-resources"
HEAD = "2026 中国区 · 新客户与新项目"
TOTAL = 9


def font(size, bold=False):
    name = "msyhbd.ttc" if bold else "msyh.ttc"
    return ImageFont.truetype(f"C:/Windows/Fonts/{name}", size)


f_h1 = font(74, True)
f_h2 = font(52, True)
f_h3 = font(40, True)
f_body = font(34)
f_tiny = font(24)
f_num = font(96, True)


def wrap(s, fnt, maxw, draw):
    lines, cur = [], ""
    for ch in s:
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


def text(draw, xy, s, fnt, fill=DARK, maxw=None, spacing=1.36):
    x, y = xy
    lh = int(fnt.size * spacing)
    for para in s.split("\n"):
        lines = wrap(para, fnt, maxw, draw) if maxw else [para]
        for ln in lines:
            draw.text((x, y), ln, fill=fill, font=fnt)
            y += lh
    return y


def newpage():
    img = Image.new("RGB", (W, H), "#FFFFFF")
    return img, ImageDraw.Draw(img)


def header(draw, idx, title, subtitle=None, accent=RED):
    draw.rectangle([0, 0, W, 14], fill=accent)
    draw.rounded_rectangle([64, 60, 90, 86], radius=7, fill=accent)
    text(draw, (104, 56), HEAD, font(27, True), GRAY)
    pg = f"{idx:02d}/{TOTAL:02d}"
    draw.text((W - 64 - draw.textlength(pg, font=font(28, True)), 56),
              pg, fill=GRAY, font=font(28, True))
    y = 124
    y = text(draw, (64, y), title, f_h2, DARK, W - 128)
    if subtitle:
        y = text(draw, (64, y + 14), subtitle, f_body, GRAY, W - 128)
    draw.line([64, FOOT, W - 64, FOOT], fill=LINE, width=2)
    draw.text((64, H - 74), BRAND, fill=GRAY, font=f_tiny)
    right = "开源 · 免费 · 无广告"
    draw.text((W - 64 - draw.textlength(right, font=f_tiny), H - 74),
              right, fill=GRAY, font=f_tiny)
    return y + 36


def pill(draw, x, y, s, fg=RED, bg="#FFFFFF", fnt=None, padx=17, pady=7):
    fnt = fnt or font(24, True)
    w = draw.textlength(s, font=fnt)
    draw.rounded_rectangle([x, y, x + w + padx * 2, y + fnt.size + pady * 2],
                           radius=(fnt.size + pady * 2) // 2, fill=bg)
    draw.text((x + padx, y + pady - 2), s, fill=fg, font=fnt)
    return y + fnt.size + pady * 2


def client_card(draw, y, name, tags, lines, note, height=372):
    draw.rounded_rectangle([64, y, W - 64, y + height], radius=26, fill=LIGHT)
    draw.rounded_rectangle([90, y + 30, 98, y + 76], radius=4, fill=RED)
    tx = 118
    nw = W - 64 - tx - 30
    text(draw, (tx, y + 24), name, f_h3, DARK, nw)
    px, ty = tx, y + 84
    for t in tags:
        tw = draw.textlength(t, font=font(24, True)) + 34
        if px + tw > W - 94:
            px, ty = tx, ty + 52
        pill(draw, px, ty, t, RED, "#FFFFFF")
        px += tw + 12
    ly = y + 148
    for ln in lines:
        draw.ellipse([tx + 2, ly + 11, tx + 12, ly + 21], fill=RED)
        ly = text(draw, (tx + 30, ly), ln, font(29), GRAY, nw - 34, 1.28) + 8
    draw.line([tx, y + height - 58, W - 94, y + height - 58], fill=LINE, width=2)
    nl = text(draw, (tx, y + height - 46), note, font(24, True), DEEP, nw)
    print(f"  card y={y} lines_end={int(ly)} limit={y + height - 58} note_end={int(nl)}")
    return y + height + 40


def source_bar(draw, y, s, h=88):
    draw.rounded_rectangle([64, y, W - 64, y + h], radius=18, fill="#FFFFFF",
                           outline=LINE, width=2)
    text(draw, (92, y + 20), s, font(24), GRAY, W - 184, 1.3)
    return y + h


# ================= 01 封面 =================
img = Image.new("RGB", (W, H), DEEP)
d = ImageDraw.Draw(img)
for x in range(W):
    t = x / W
    d.line([(x, 0), (x, H)], fill=(int(0xA8 + 0x3C * t), 0, int(0x1B + 0x10 * t)))
d.ellipse([W - 340, H - 460, W + 150, H + 30], outline="#FFFFFF", width=2)
d.ellipse([W - 240, -180, W + 210, 270], outline="#FFFFFF", width=2)

d.rounded_rectangle([64, 68, 470, 114], radius=23, fill="#FFFFFF")
d.text((88, 75), "INFOR · 中国市场观察", fill=DEEP, font=font(25, True))

y = 182
y = text(d, (64, y), "2026 Infor 中国区", f_h1, "#FFFFFF", W - 128)
y = text(d, (64, y - 6), "新客户与新项目", f_h1, GOLD, W - 128)
y = text(d, (64, y + 34), "官方一年没发几条稿，我从实施商、\n客户侧和工商信息里把节点挖出来了",
         font(34), "#FFE3E6", W - 128, 1.5)

by = y + 40
blocks = [("4", "本土新客户"), ("2", "海外交付节点"), ("7", "可查时间点")]
bw = (W - 128 - 40) // 3
for i, (n, label) in enumerate(blocks):
    bx = 64 + i * (bw + 20)
    d.rounded_rectangle([bx, by, bx + bw, by + 214], radius=24,
                        outline="#FFFFFF", width=2)
    d.text((bx + 30, by + 26), n, fill=GOLD, font=f_num)
    text(d, (bx + 30, by + 148), label, font(27, True), "#FFFFFF", bw - 44)

d.line([64, H - 190, W - 64, H - 190], fill="#FFFFFF", width=2)
text(d, (64, H - 162), "全部条目附来源链接与时间节点", font(30, True), "#FFFFFF", W - 128)
text(d, (64, H - 106), BRAND, font(30), "#FFC9D0", W - 128)
print("p01 bottom", by + 214)
img.save(OUT / "01-cover.png")

# ================= 02 口径 =================
img, d = newpage()
y = header(d, 2, "先说口径：这份清单怎么来的",
           "不写「据说」，只留有明确来源 + 明确时间点的条目")

items = [
    ("官方渠道缺位", "infor.cn 没有本地新闻栏目，客户故事清一色是海外案例（Bozeman Health、Combilift 这类）"),
    ("官宣主体在伙伴", "中国区客户动态基本由拓创数信、润数科技、得宝易等实施伙伴代发"),
    ("搜索覆盖有限", "公众号内容未被搜索引擎完整索引，能挖到的是网页端可检索的部分"),
    ("采购多不公开", "这类项目以直接采购 / 单一来源为主，招标平台鲜有 Infor 中标公告"),
]
for i, (t, b) in enumerate(items):
    ty = y + i * 214
    d.rounded_rectangle([64, ty, W - 64, ty + 190], radius=24, fill=LIGHT)
    d.ellipse([96, ty + 36, 152, ty + 92], fill=RED)
    num = str(i + 1)
    d.text((96 + (56 - d.textlength(num, font=font(30, True))) / 2, ty + 43),
           num, fill="#FFFFFF", font=font(30, True))
    text(d, (176, ty + 32), t, f_h3, DARK, W - 260)
    text(d, (176, ty + 94), b, font(28), GRAY, W - 260, 1.36)

by = y + 4 * 214 + 2
d.rounded_rectangle([64, by, W - 64, by + 112], radius=22, fill=PALE)
text(d, (96, by + 30), "「公开可见」≠「全部签约」，也不代表项目金额与规模。",
     font(29, True), DEEP, W - 192)
print("p02 bottom", by + 112)
img.save(OUT / "02-scope.png")

# ================= 03 时间线 =================
img, d = newpage()
y = header(d, 3, "2026 全年时间线", "按官网、伙伴新闻与工商公示可核实的时间点排序")

tl = [
    ("02-04", "Infor 亚太区领导层调整", "大中华区并入 SENA 统一管理"),
    ("03-04", "中秦兴龙 · 项目启动会", "汽车铝合金车轮 / 底盘转向节｜拓创数信"),
    ("03-13", "Toyo 东南亚工厂 · 启动", "CloudSuite Enterprise（LN 云）｜拓创数信"),
    ("04-01", "英赛斯 · 项目启动", "生物医药 CMC 工艺装备｜拓创数信"),
    ("04-13", "易开迪 EKT · 启动公布", "工业锂电池 / 充电机，覆盖 43 国｜润数科技"),
    ("07-01", "Toyo 美国工厂 · Go-Live", "生产 / 供应链 / 财务 / 合规溯源全量切换"),
    ("07-25", "德生堂 壹壹壹云仓 · 投运", "北京平谷，Infor WMS 日处理 5 万单"),
    ("08-21", "恩富（中国）· 法人变更", "顾峰 → LEE WENG KHUEN（工商公示）"),
]
top = y + 8
gap = 112
d.line([222, top + 36, 222, top + gap * (len(tl) - 1) + 36], fill=LINE, width=3)
for i, (dt, title, sub) in enumerate(tl):
    ry = top + i * gap
    col = RED if i in (1, 3, 4, 6) else "#B4B8BE"
    d.text((64, ry + 8), dt, fill=col, font=font(30, True))
    d.ellipse([208, ry + 22, 236, ry + 50], fill=col, outline="#FFFFFF", width=3)
    text(d, (268, ry), title, font(33, True), DARK, W - 300)
    text(d, (268, ry + 46), sub, font(25), GRAY, W - 300)
print("p03 bottom", top + gap * 7 + 46 + 34)
img.save(OUT / "03-timeline.png")

# ================= 04 本土客户 A =================
img, d = newpage()
y = header(d, 4, "本土新客户 ①", "汽车零部件 + 生物医药装备，都是「新签 + 新启动」")

y2 = client_card(
    d, y + 2, "秦皇岛中秦兴龙工业集团",
    ["汽车零部件", "Infor ERP"],
    ["铝合金车轮 1,700 万只/年，转向节 1,400 万只",
     "配套奔驰、宝马、奥迪、大众、丰田等主机厂",
     "打通生产、供应链、财务全链路，支撑海外拓展"],
    "2026-03-04 启动会｜拓创数信｜原文只写「Infor ERP 解决方案」",
)
y3 = client_card(
    d, y2, "苏州英赛斯智能科技",
    ["生物医药装备", "Infor LN"],
    ["CMC 工艺装备：核酸合成、纳米药物制备",
     "国家级专精特新「小巨人」、苏州独角兽",
     "打通研发—生产—财务数据孤岛，服务全球交付"],
    "2026-04-01 启动｜计划 2026 下半年上线｜拓创数信",
)
source_bar(d, y3 + 4, "来源：拓创数信项目新闻（2026-03-04 中秦兴龙、2026-04-01 英赛斯）与客户方公开报道。")
print("p04 bottom", y3 + 4 + 88)
img.save(OUT / "04-clients-a.png")

# ================= 05 本土客户 B =================
img, d = newpage()
y = header(d, 5, "本土新客户 ②", "新能源出海 + 医药流通，两个非典型的 LN 与 WMS 场景")

y2 = client_card(
    d, y + 2, "易开迪集团（EKT）",
    ["新能源", "43 国业务", "Infor LN"],
    ["工业锂电池、高频智能充电机",
     "业务覆盖 43 个国家，出口占比高",
     "目标：建全球统一的数字化管理中枢"],
    "2026-04-13 公布启动｜润数科技",
)
y3 = client_card(
    d, y2, "德生堂集团 壹壹壹智慧云仓",
    ["医药流通", "北京平谷", "Infor WMS"],
    ["北京首家药品批零一体化合规医药智慧仓",
     "1 万+ m²，日处理订单可达 5 万单",
     "SAP + RELEX + Infor WMS 组合"],
    "2026-07-25 启用｜客户主动公开披露的落地项目",
)
source_bar(d, y3 + 4, "来源：润数科技案例页；中国商报 / 新浪财经 / 中国商业联合会 2026-07-25 前后报道。")
print("p05 bottom", y3 + 4 + 88)
img.save(OUT / "05-clients-b.png")

# ================= 06 Toyo 海外双节点 =================
img, d = newpage()
y = header(d, 6, "中国实施商交付的海外项目",
           "同一套 CloudSuite，从东南亚基地推到美国首座工厂")

d.rounded_rectangle([64, y + 4, W - 64, y + 328], radius=26, fill=LIGHT)
steps = [("03-13", "东南亚基地", "项目启动"), ("07-01", "美国首座工厂", "Go-Live 上线")]
sw = 372
for i, (dt, place, state) in enumerate(steps):
    sx = 96 + i * (sw + 96)
    d.rounded_rectangle([sx, y + 42, sx + sw, y + 290], radius=20, fill="#FFFFFF",
                        outline=RED, width=3)
    d.text((sx + 26, y + 66), dt, fill=RED, font=font(34, True))
    text(d, (sx + 26, y + 120), place, f_h3, DARK, sw - 52)
    d.text((sx + 26, y + 196), state, fill=GRAY, font=font(30, True))
d.polygon([(510, y + 148), (510, y + 190), (546, y + 169)], fill=RED)

caps = ["批次 / 序列号全链路追溯", "多工厂统一管控与合规溯源",
        "需求调研 → 数据迁移 → 全员培训 → 多轮压测"]
cy = y + 366
for i, c in enumerate(caps):
    if i % 2 == 0:
        d.rounded_rectangle([64, cy - 4, W - 64, cy + 82], radius=16, fill=LIGHT)
    d.ellipse([92, cy + 24, 114, cy + 46], fill=RED)
    text(d, (134, cy + 18), c, font(30), DARK, W - 220)
    cy += 96

d.rounded_rectangle([64, cy + 2, W - 64, cy + 190], radius=20, fill="#FFF8E1")
text(d, (96, cy + 26), "口径提醒：报道只称「Toyo」，未给注册主体",
     font(28, True), "#8A6D00", W - 192)
text(d, (96, cy + 74), "建议写「拓创交付的 Toyo 海外工厂项目」，不要直接认定为中国本土客户或日本东洋轮胎。",
     font(25), "#8A6D00", W - 192, 1.34)
text(d, (96, cy + 148), "来源：拓创数信 2026-03-13 启动稿、2026-07-21 Go-Live 稿",
     font(23), "#A8873A", W - 192)
print("p06 bottom", cy + 190)
img.save(OUT / "06-overseas.png")

# ================= 07 跨年度 CNH =================
img, d = newpage()
y = header(d, 7, "跨年度延续：凯斯纽荷兰 CNH",
           "2025-10-31 签约并启动，实施周期跨进 2026")

nums = [("14", "年", "双方合作基础"), ("3", "地", "仓库覆盖城市"), ("2", "套", "ERP + WMS")]
nw = (W - 128 - 32) // 3
for i, (n, unit, label) in enumerate(nums):
    bx = 64 + i * (nw + 16)
    d.rounded_rectangle([bx, y + 4, bx + nw, y + 236], radius=22, fill=PALE)
    d.text((bx + 26, y + 28), n, fill=RED, font=font(84, True))
    d.text((bx + 26 + d.textlength(n, font=font(84, True)) + 10, y + 82), unit,
           fill=RED, font=font(30, True))
    text(d, (bx + 26, y + 164), label, font(26, True), GRAY, nw - 50)

cy = y + 278
rows = [
    ("签约节点", "2025-10-31 公布，项目启动会在上海总部召开"),
    ("覆盖范围", "ERP 财务 / 供应链核心流程升级 + WMS 覆盖上海、哈尔滨、乌鲁木齐三地仓库"),
    ("项目定位", "农机头部企业的「ERP + WMS 一体化」智慧仓储标杆，并与全球运营系统集成"),
]
for i, (k, v) in enumerate(rows):
    ry = cy + i * 196
    d.rounded_rectangle([64, ry, W - 64, ry + 176], radius=22, fill=LIGHT)
    d.text((96, ry + 26), k, fill=RED, font=font(28, True))
    text(d, (96, ry + 78), v, font(30), DARK, W - 192, 1.36)

zy = cy + 3 * 196
text(d, (64, zy), "存量客户愿意升级，比新签更能说明「用得住」。", font(29, True), GRAY, W - 128)
text(d, (64, zy + 48), "来源：拓创数信 2025-10-31 签约稿；项目周期跨入 2026。",
     font(24), "#999999", W - 128)
print("p07 bottom", zy + 48 + 34)
img.save(OUT / "07-cnh.png")

# ================= 08 组织与生态 =================
img, d = newpage()
y = header(d, 8, "组织与生态侧的两个信号",
           "不涉及客户名，但能解释中国区为什么越来越靠伙伴")

cards = [
    ("2026-02-04", "亚太区（APJ）领导层调整",
     ["Geoff Thomas 出任 APJ 高级副总裁兼总经理",
      "Victor Ng 扩权为 SENA（东盟 + 大中华区 + 韩国）副总裁兼董事总经理，常驻新加坡"]),
    ("2026-08-21", "恩富软件（中国）法定代表人变更",
     ["由顾峰变更为 LEE WENG KHUEN",
      "监事由 ILJA GIANI 接替 ANDRE P HYLTON；不代表业务策略变更"]),
]
cy = y + 2
for i, (dt, t, ls) in enumerate(cards):
    ry = cy + i * 292
    d.rounded_rectangle([64, ry, W - 64, ry + 276], radius=24, fill=LIGHT)
    d.rounded_rectangle([96, ry + 28, 104, ry + 116], radius=4, fill=RED)
    d.text((122, ry + 24), dt, fill=RED, font=font(28, True))
    text(d, (122, ry + 68), t, f_h3, DARK, W - 220)
    yy = ry + 130
    for ln in ls:
        d.ellipse([124, yy + 12, 134, yy + 22], fill=RED)
        yy = text(d, (150, yy), ln, font(27), GRAY, W - 240, 1.34) + 8

ry = cy + 2 * 292 + 8
d.rounded_rectangle([64, ry, W - 64, ry + 258], radius=24, fill="#FFFFFF",
                    outline=RED, width=3)
d.text((96, ry + 24), "云部署的硬约束", fill=RED, font=font(28, True))
text(d, (96, ry + 74),
     "CloudSuite 为 AWS 多租户云，官方口径 10 个 Region / 27 个可用区，不含中国大陆 Region。",
     font(29), DARK, W - 192, 1.36)
text(d, (96, ry + 172),
     "所以中国实体多走本地部署 / 混合架构，或先用 WMS、FT、BI 这类单点产品切入。",
     font(27), GRAY, W - 192, 1.34)

sy = ry + 258 + 18
d.rounded_rectangle([64, sy, W - 64, sy + 104], radius=20, fill=PALE)
text(d, (96, sy + 24), "对从业者的含义：伙伴交付能力 + 存量升级，比新签更值得盯。",
     font(28, True), DEEP, W - 192, 1.34)
print("p08 bottom", sy + 104)
img.save(OUT / "08-ecosystem.png")

# ================= 09 双入口二维码 =================
img, d = newpage()
y = header(d, 9, "两个入口，内容同一份",
           "国内镜像站打开更快；GitHub Pages 是原始发布源，两边页面完全一致")

URL_CN = "https://infor-ecosystem-open-resources.cuiwenyuan.cn/resources/news/"
URL_GH = "https://cuiwenyuan.github.io/infor-ecosystem-open-resources/resources/news/"


def make_qr(url, size):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,
                      box_size=12, border=3)
    q.add_data(url)
    q.make(fit=True)
    return q.make_image(fill_color=DARK, back_color="white").convert("RGB").resize(
        (size, size), Image.LANCZOS)


CW, CH, QS = 460, 612, 360
cards = [
    (64, "国内镜像站 · 推荐", ["infor-ecosystem-open-resources", ".cuiwenyuan.cn"], RED, PALE),
    (64 + CW + 32, "GitHub Pages", ["cuiwenyuan.github.io", "infor-ecosystem-open-resources"], "#8A8F98", LIGHT),
]
top = y + 4
for k, (cx, label, host_lines, col, bg) in enumerate(cards):
    d.rounded_rectangle([cx, top, cx + CW, top + CH], radius=26, fill=bg)
    d.rounded_rectangle([cx, top, cx + CW, top + CH], radius=26, outline=col, width=3)
    lf = font(24, True)
    lw = d.textlength(label, font=lf)
    d.rounded_rectangle([cx + (CW - lw) / 2 - 20, top + 20, cx + (CW + lw) / 2 + 20, top + 20 + 46],
                        radius=23, fill=col)
    d.text((cx + (CW - lw) / 2, top + 29), label, fill="#FFFFFF", font=lf)
    img.paste(make_qr(URL_CN if k == 0 else URL_GH, QS), (cx + (CW - QS) // 2, top + 90))
    ly = top + 472
    for ln in host_lines:
        ly = text(d, (cx + 30, ly), ln, font(22, True), DARK if k == 0 else "#4A4F57", CW - 60, 1.24)
    text(d, (cx + 30, ly + 4), "→ /resources/news/", font(21), GRAY, CW - 60)

d.rounded_rectangle([64, top + CH + 20, W - 64, top + CH + 110], radius=22, fill=PALE)
hint = "微信内长按对应二维码 · 都直达「行业动态」页"
d.text(((W - d.textlength(hint, font=font(29, True))) / 2, top + CH + 46),
       hint, fill=DEEP, font=font(29, True))

fy = top + CH + 168
text(d, (64, fy), "国内镜像站：自托管字体、页面零境外前端请求，实测约 0.1 秒（3 次均值 0.10s）",
     font(23), "#666666", W - 128, 1.3)
text(d, (64, fy + 48), "GitHub Pages：原始发布源，国内访问 0.9~7 秒，偶有超时",
     font(23), "#999999", W - 128, 1.3)
print("p09 bottom", fy + 48 + 30)

make_qr(URL_CN, 660).save(OUT / "qrcode-cn.png")
make_qr(URL_GH, 660).save(OUT / "qrcode-github-pages.png")
img.save(OUT / "09-qrcode.png")

print("done:", len(list(OUT.glob("0*.png"))), "images")
