# -*- coding: utf-8 -*-
"""公众号封面图 2.35:1 (900x383) — LN Session 速查"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pathlib import Path

OUT = Path(__file__).parent
W, H = 900, 383

img = Image.new("RGB", (W, H), "#E4002B")
draw = ImageDraw.Draw(img)

# 深红渐变背景（左深右浅）
for x in range(W):
    t = x / W
    r = int(0xB8 + (0xE4 - 0xB8) * t)
    g = int(0x00 + (0x00 - 0x00) * t)
    b = int(0x1F + (0x2B - 0x1F) * t)
    draw.line([(x, 0), (x, H)], fill=(r, g, b))

# 装饰: 右下大圆弧半透明
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od = ImageDraw.Draw(overlay)
od.ellipse([W - 260, H - 260, W + 60, H + 60], fill=(255, 255, 255, 22))
od.ellipse([W - 170, -110, W + 90, 150], fill=(255, 255, 255, 16))
img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
draw = ImageDraw.Draw(img)

def font(size, bold=False):
    name = "msyhbd.ttc" if bold else "msyh.ttc"
    return ImageFont.truetype(f"C:/Windows/Fonts/{name}", size)

f_main = font(54, bold=True)
f_sub = font(30)
f_pill = font(22)
f_brand = font(24, bold=True)

# 主标题（两行式主视觉）: 自动缩字号确保不超宽
t_main = "Infor LN ERP Session"
size = 54
while size > 30:
    f_main = font(size, bold=True)
    if draw.textlength(t_main, font=f_main) <= W - 112:
        break
    size -= 2
draw.text((56, 84), t_main, fill="#FFFFFF", font=f_main)
draw.text((56, 158), "中英速查表", fill="#FFD54F", font=f_main)

# 副标题
draw.text((58, 246), "中英双语 · 模糊搜索 · 扫码即用", fill=(255, 255, 255, 220), font=f_sub)

# 装饰 pills: 常用 session code（半透明需在 RGBA overlay 上画）
overlay2 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
od2 = ImageDraw.Draw(overlay2)
pills = ["tdsls4100m000", "tfgld1101m000", "ttaad2500m000"]
px, py = 58, 316
for p in pills:
    w = draw.textlength(p, font=f_pill)
    od2.rounded_rectangle([px - 10, py - 6, px + w + 10, py + 32], radius=18,
                          fill=(255, 255, 255, 40), outline=(255, 255, 255, 130), width=1)
    od2.text((px, py), p, fill=(255, 255, 255, 235), font=f_pill)
    px += w + 34
img = Image.alpha_composite(img.convert("RGBA"), overlay2).convert("RGB")

# 右侧品牌库徽标块
brand = "infor-ecosystem-open-resources"
bw = draw.textlength(brand, font=f_brand)
bx = W - bw - 48
draw.rounded_rectangle([bx - 18, 44, W - 30, 92], radius=24, fill=(255, 255, 255, 235))
draw.text((bx, 52), brand, fill="#B80023", font=f_brand)

img.save(OUT / "cover-2.35.png")
print("cover saved:", img.size)
