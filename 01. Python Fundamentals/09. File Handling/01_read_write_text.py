# 01 — Read and write text files
# Run: python 01_read_write_text.py

import os

filename = "sample_notes.txt"

# --- 1. Write ---
with open(filename, "w", encoding="utf-8") as f:
    f.write("Line one\n")
    f.write("Line two\n")
    f.writelines(["Line three\n", "Line four\n"])

print("Wrote", filename)

# --- 2. Read entire file ---
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()
print("--- read() ---")
print(content)

# --- 3. Read line by line ---
print("--- readlines() ---")
with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())

# --- 4. Append mode ---
with open(filename, "a", encoding="utf-8") as f:
    f.write("Appended line\n")

# --- Cleanup demo file ---
os.remove(filename)
print("Removed", filename)
