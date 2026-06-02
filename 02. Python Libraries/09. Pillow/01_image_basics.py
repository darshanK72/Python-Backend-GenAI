# 01 — Pillow (PIL) image basics
# Notebook (recommended): 01-pillow.ipynb  (inline display)
# Run: python 01_image_basics.py

from PIL import Image, ImageDraw
import os

# --- 1. Create image ---
img = Image.new("RGB", (200, 120), color=(70, 130, 180))
draw = ImageDraw.Draw(img)
draw.rectangle([20, 20, 180, 100], outline="white", width=3)
draw.text((50, 50), "Hello", fill="white")
img.save("demo_pillow.png")
print("saved demo_pillow.png")

# --- 2. Open and inspect ---
opened = Image.open("demo_pillow.png")
print("size:", opened.size, "mode:", opened.mode)

# --- 3. Resize thumbnail ---
thumb = opened.copy()
thumb.thumbnail((80, 80))
thumb.save("demo_thumb.png")
print("thumbnail saved")

opened.close()
os.remove("demo_pillow.png")
os.remove("demo_thumb.png")
