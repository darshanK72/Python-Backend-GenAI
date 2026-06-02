# 07 — Display images (PhotoImage)
# Run: python 07_photo_image.py
# Place images in the images/ folder next to this file.

from pathlib import Path
from tkinter import Tk, Label

AUTO_CLOSE_MS = 3000

app = Tk()
app.title("Image viewer")

images_dir = Path(__file__).parent / "images"
candidates = list(images_dir.glob("*.png")) + list(images_dir.glob("*.jpg")) + list(images_dir.glob("*.jpeg"))

if not candidates:
    Label(app, text=f"No images in {images_dir}").pack(padx=20, pady=20)
else:
    img_path = candidates[0]
    # PhotoImage supports GIF natively; PNG/JPEG on Tk 8.6+
    from tkinter import PhotoImage
    photo = PhotoImage(file=str(img_path))
    label = Label(app, image=photo)
    label.image = photo   # keep reference
    label.pack()
    Label(app, text=img_path.name).pack()

if AUTO_CLOSE_MS:
    app.after(AUTO_CLOSE_MS, app.destroy)
app.mainloop()
