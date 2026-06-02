# 06 — messagebox dialogs
# Run: python 06_messagebox.py
# Set AUTO_CLOSE_MS = None and click buttons to test dialogs.

from tkinter import Tk, Button
from tkinter import messagebox

AUTO_CLOSE_MS = None

app = Tk()
app.title("Dialogs")
app.geometry("300x150")

def show_info():
    messagebox.showinfo("Info", "Saved successfully!")

def show_confirm():
    ok = messagebox.askyesno("Confirm", "Delete this item?")
    print("User chose:", ok)

Button(app, text="Show info", command=show_info).pack(pady=10)
Button(app, text="Confirm", command=show_confirm).pack()

if AUTO_CLOSE_MS:
    app.after(AUTO_CLOSE_MS, app.destroy)
app.mainloop()
