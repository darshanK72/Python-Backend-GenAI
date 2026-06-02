# 03 — Buttons and commands
# Run: python 03_buttons.py

from tkinter import Tk, Button, Label

AUTO_CLOSE_MS = 2500

app = Tk()
app.geometry("320x200")
counter = {"n": 0}
label = Label(app, text="Count: 0", font=("Segoe UI", 14))
label.pack(pady=15)

def increment():
    counter["n"] += 1
    label.config(text=f"Count: {counter['n']}")

Button(app, text="Click me", command=increment, padx=20, pady=10).pack()
Button(app, text="Quit", command=app.destroy).pack(pady=5)

if AUTO_CLOSE_MS:
    app.after(AUTO_CLOSE_MS, app.destroy)
app.mainloop()
