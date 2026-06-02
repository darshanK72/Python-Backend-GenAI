# 04 — Entry widgets and grid layout (mini calculator)
# Run: python 04_entry_calculator.py
# Set AUTO_CLOSE_MS = None to use the calculator interactively.

import tkinter as tk

AUTO_CLOSE_MS = None   # interactive demo — no auto-close

root = tk.Tk()
root.title("Add Two Numbers")
root.geometry("360x180")

num1 = tk.StringVar()
num2 = tk.StringVar()
result_text = tk.StringVar(value="Result: —")

def calculate():
    try:
        a = int(num1.get())
        b = int(num2.get())
        result_text.set(f"Result: {a + b}")
    except ValueError:
        result_text.set("Result: invalid input")

tk.Label(root, text="A").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=num1).grid(row=0, column=1, padx=5, pady=5)
tk.Label(root, text="B").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=num2).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Calculate", command=calculate).grid(row=2, column=0, columnspan=2, pady=10)
tk.Label(root, textvariable=result_text).grid(row=3, column=0, columnspan=2)

if AUTO_CLOSE_MS:
    root.after(AUTO_CLOSE_MS, root.destroy)
root.mainloop()
