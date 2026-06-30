# 12 — Nested loops (loop inside a loop)
# Run: python 12_nested_loops.py

# --- 1. Nested for — pairs (i, j) ---
print("--- 3x3 grid ---")
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print()

# --- 2. Multiplication table row (1 to 5) ---
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()

# --- 3. Nested while ---
i = 1
while i < 4:
    j = 1
    while j < 4:
        print(i, j)
        j += 1
    i += 1

# --- 4. Pattern: print stars (right triangle) ---
for row in range(1, 6):
    for col in range(row):
        print("*", end="")
    print()
