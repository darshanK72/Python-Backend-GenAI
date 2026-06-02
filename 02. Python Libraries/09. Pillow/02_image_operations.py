# 02 — Crop, rotate, convert mode
# Run: python 02_image_operations.py

from PIL import Image, ImageFilter
import os

img = Image.new("RGB", (300, 200), (200, 100, 50))
path = "sample.jpg"
img.save(path)

# --- Crop box (left, upper, right, lower) ---
im = Image.open(path)
cropped = im.crop((50, 30, 250, 170))
rotated = cropped.rotate(45, expand=True)
rotated.save("rotated.png")

# --- Grayscale ---
gray = im.convert("L")
gray.save("gray.png")

# --- Filter ---
blurred = im.filter(ImageFilter.GaussianBlur(radius=2))
blurred.save("blurred.png")

im.close()
for f in [path, "rotated.png", "gray.png", "blurred.png"]:
    os.remove(f)
print("operations demo OK")
