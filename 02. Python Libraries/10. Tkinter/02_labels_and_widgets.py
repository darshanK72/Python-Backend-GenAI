# 02 — Labels, fonts, and colors
# Run: python 02_labels_and_widgets.py

from tkinter import Tk, Label, StringVar

AUTO_CLOSE_MS = 2000

app = Tk()
app.title("Labels")
app.configure(bg="#f0f0f0")

status = StringVar(value="Ready")
Label(app, text="Python GUI", font=("Segoe UI", 18, "bold"), fg="#2c3e50").pack(pady=10)
Label(app, textvariable=status, fg="gray").pack()
status.set("All systems go")

if AUTO_CLOSE_MS:
    app.after(AUTO_CLOSE_MS, app.destroy)
app.mainloop()
