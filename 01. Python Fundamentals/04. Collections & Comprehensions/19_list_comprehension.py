# 01 — List comprehension
# Run: python 01_list_comprehension.py
#
# [expression for item in iterable if condition]
# Replaces many simple for-loops that build a list.

# --- 1. Classic loop vs comprehension ---
evens_loop = []
for i in range(21):
    if i % 2 == 0:
        evens_loop.append(i)

evens = [i for i in range(21) if i % 2 == 0]
print("same result:", evens_loop == evens)

# --- 2. Transform each item ---
squares = [x ** 2 for x in range(1, 11)]
print("squares:", squares)

# --- 3. From a string ---
letters = [ch.upper() for ch in "python" if ch != "o"]
print("letters:", letters)

# --- 4. Nested loop (flatten pairs) ---
pairs = [(x, y) for x in range(1, 4) for y in range(1, 3)]
print("pairs:", pairs)
