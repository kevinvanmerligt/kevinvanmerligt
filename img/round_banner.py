from PIL import Image, ImageDraw

PATH = "img/banner.png"
RADIUS_RATIO = 0.025  # makin besar makin bulat

img = Image.open(PATH).convert("RGBA")
w, h = img.size
radius = int(w * RADIUS_RATIO)

scale = 4
mask = Image.new("L", (w * scale, h * scale), 0)
ImageDraw.Draw(mask).rounded_rectangle(
    (0, 0, w * scale - 1, h * scale - 1), radius=radius * scale, fill=255
)
mask = mask.resize((w, h), Image.LANCZOS)

img.putalpha(mask)
img.save(PATH, "PNG")
print(f"Selesai: {PATH} ({w}x{h}, radius {radius}px)")
