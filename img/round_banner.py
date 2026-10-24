"""Bikin sudut banner sedikit rounded.

Cara pakai (jalankan dari root folder repo):
    pip install pillow
    python round_banner.py

Input : img/banner.jpg
Output: img/banner.png (PNG transparan, sudut rounded)
"""
from PIL import Image, ImageDraw

SRC = "img/banner.jpg"
DST = "img/banner.png"
RADIUS_RATIO = 0.025  # 2.5% dari lebar gambar -> rounded tipis. Naikkan kalau mau lebih bulat.

img = Image.open(SRC).convert("RGBA")
w, h = img.size
radius = int(w * RADIUS_RATIO)

# Supersampling 4x biar tepi sudut halus (anti-aliasing)
scale = 4
mask = Image.new("L", (w * scale, h * scale), 0)
ImageDraw.Draw(mask).rounded_rectangle(
    (0, 0, w * scale - 1, h * scale - 1), radius=radius * scale, fill=255
)
mask = mask.resize((w, h), Image.LANCZOS)

img.putalpha(mask)
img.save(DST, "PNG")
print(f"Selesai: {DST} ({w}x{h}, radius {radius}px)")
