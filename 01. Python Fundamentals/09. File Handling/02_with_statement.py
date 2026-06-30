# 02 — with statement (context manager)
# Run: python 02_with_statement.py
#
# with ensures files are closed even if an error occurs.

import os

path = "demo_with.txt"

# --- 1. Without with (easy to forget close) ---
f = open(path, "w", encoding="utf-8")
f.write("hello")
f.close()

# --- 2. With with (preferred) ---
with open(path, "w", encoding="utf-8") as f:
    f.write("safe write\n")
    # f.close() called automatically when block ends

with open(path, "r", encoding="utf-8") as f:
    print(f.read())

# --- 3. Multiple context managers ---
with open(path, "r", encoding="utf-8") as src, open("copy.txt", "w", encoding="utf-8") as dst:
    dst.write(src.read())

os.remove(path)
os.remove("copy.txt")
print("Cleanup done")
