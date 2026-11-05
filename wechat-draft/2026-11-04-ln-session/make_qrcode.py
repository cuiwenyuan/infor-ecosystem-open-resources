# -*- coding: utf-8 -*-
"""生成 LN Session 页面二维码（公众号文章用）"""
import qrcode
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path(__file__).parent
URL = "https://cuiwenyuan.github.io/infor-ecosystem-open-resources/resources/ln-sessions/"

# 1) 纯二维码（黑白高对比, ECC=H, 适合微信长按识别）
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=12, border=4)
qr.add_data(URL)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(OUT / "qrcode-plain.png")
print("plain:", img.size)

# 2) 卡片版：二维码 + 网址 + 提示语（900px 宽，适合文章插图）
W = 900
card = Image.new("RGB", (W, 1130), "#FFFFFF")
draw = ImageDraw.Draw(card)

# 边框圆角卡片感: 顶部红色条
draw.rectangle([0, 0, W, 14], fill="#E4002B")

# 加载字体（微软雅黑）
def font(size, bold=False):
    name = "msyhbd.ttc" if bold else "msyh.ttc"
    try:
        return ImageFont.truetype(f"C:/Windows/Fonts/{name}", size)
    except Exception:
        return ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", size)

f_title = font(44, bold=True)
f_sub = font(30)
pass
f_hint = font(32, bold=True)

# 标题
t1 = "Infor LN Session 速查"
t2 = "12,125 条 Session · 多版本文档 · 即搜即达"
w1 = draw.textlength(t1, font=f_title)
w2 = draw.textlength(t2, font=f_sub)
draw.text(((W - w1) / 2, 60), t1, fill="#1A1A1A", font=f_title)
draw.text(((W - w2) / 2, 130), t2, fill="#E4002B", font=f_sub)

# 二维码居中（缩到 620px）
qimg = Image.open(OUT / "qrcode-plain.png").resize((620, 620), Image.LANCZOS)
card.paste(qimg, ((W - 620) // 2, 210))

# 网址（两行显示，避免截断）
f_url = font(28)
u1 = "cuiwenyuan.github.io/infor-ecosystem-open-resources"
u2 = "/resources/ln-sessions/"
w1 = draw.textlength(u1, font=f_url)
w2 = draw.textlength(u2, font=f_url)
draw.text(((W - w1) / 2, 852), u1, fill="#555555", font=f_url)
draw.text(((W - w2) / 2, 894), u2, fill="#555555", font=f_url)

# 提示
h = "微信长按识别二维码 · 一键直达"
w4 = draw.textlength(h, font=f_hint)
draw.text(((W - w4) / 2, 960), h, fill="#E4002B", font=f_hint)

# 底部淡灰品牌
f_brand = font(26)
b = "Infor 生态开放资源导航 · infor-ecosystem-open-resources"
wb = draw.textlength(b, font=f_brand)
draw.text(((W - wb) / 2, 1040), b, fill="#999999", font=f_brand)

card.save(OUT / "qrcode-card.png")
print("card saved:", card.size)
