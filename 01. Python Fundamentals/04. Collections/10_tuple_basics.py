# 10 — Tuples: create, access, immutability
# Run: python 10_tuple_basics.py
#
# Tuples are ordered and immutable — good for fixed records.

t1 = (1, 2, 3, 4, 5)
print("t1:", t1, type(t1))

# --- 1. Parentheses optional for packing ---
t2 = 5, 26, 73, 23
print("t2:", t2, type(t2))

# --- 2. Single-element tuple needs a comma ---
single = (42,)
print("single:", single, type(single))
not_tuple = (42)
print("not_tuple:", not_tuple, type(not_tuple))

# --- 3. Indexing and slicing ---
t3 = (52, 62, 13267, 3, 45, 2, 47)
print("t3[2] =", t3[2])
print("t3[-1] =", t3[-1])
print("t3[1:5] =", t3[1:5])
print("reverse:", t3[::-1])

# --- 4. Immutable ---
# t3[0] = 100   # Uncomment -> TypeError

# --- 5. Methods (only count and index) ---
print("count(3):", t3.count(3))
print("index(13267):", t3.index(13267))

# --- 6. Iterate ---
for item in t3:
    print(item, end=" ")
print()

# --- 7. Convert tuple <-> list to modify ---
t4 = (1, 2, 3)
temp = list(t4)
temp[1] = 6000
t4 = tuple(temp)
print("modified via list:", t4)
