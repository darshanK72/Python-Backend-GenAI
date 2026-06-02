# 05 — pack() and Frame
# Run: python 05_pack_and_frame.py

from tkinter import Tk, Frame, Label, Button, TOP, LEFT, X, BOTH

AUTO_CLOSE_MS = 2000

app = Tk()
app.title("Frames")

header = Frame(app, bg="#34495e", height=50)
header.pack(fill=X)
Label(header, text="Header", bg="#34495e", fg="white").pack(pady=10)

body = Frame(app, padx=10, pady=10)
body.pack(fill=BOTH, expand=True)
Label(body, text="Body content").pack(side=TOP)
Button(body, text="Action").pack(side=LEFT, padx=5)

if AUTO_CLOSE_MS:
    app.after(AUTO_CLOSE_MS, app.destroy)
app.mainloop()
