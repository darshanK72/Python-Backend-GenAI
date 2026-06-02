# 03 — Nested comprehensions
# Run: python 03_nested_comprehensions.py
#
# Use when readability is still clear. Prefer a regular loop if it gets messy.

# --- 1. Matrix (list of lists) ---
matrix = [[j for j in range(1, 4)] for i in range(3)]
print("matrix:", matrix)

# --- 2. Flatten a matrix ---
flat = [num for row in matrix for num in row]
print("flat:", flat)

# --- 3. Multiplication table row ---
table_row = [i * j for j in range(1, 6) for i in range(1, 6) if i == 3]
print("row of 3:", table_row)

# --- 4. Dict of lists ---
groups = {
    f"group_{g}": [x for x in range(g * 5, g * 5 + 5)]
    for g in range(1, 4)
}
print("groups:", groups)
