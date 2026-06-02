# 01 — Tkinter window basics
# Run: python 01_window_basics.py
# Tkinter is in the standard library on Windows (no pip install).
#
# Remove app.after(...) below to keep the window open while learning.

from tkinter import Tk, Label

AUTO_CLOSE_MS = 1500   # set to None to disable auto-close

app = Tk()
app.title("My App")
app.geometry("400x300")
app.minsize(300, 200)

title = Label(app, text="Hello, Tkinter!", font=("Segoe UI", 16))
title.pack(pady=20)

if AUTO_CLOSE_MS:
    app.after(AUTO_CLOSE_MS, app.destroy)

app.mainloop()
