# 11 — Tuple packing and unpacking
# Run: python 11_tuple_packing_unpacking.py

# --- 1. Packing — multiple values become one tuple ---
t1 = 5, 26, 73, 23
print("packed:", t1)

# --- 2. Unpacking — tuple into separate variables ---
a, b, c, d = t1
print("a,b,c,d =", a, b, c, d)

# --- 3. Swap with unpacking ---
x, y = 10, 20
x, y = y, x
print("after swap:", x, y)

# --- 4. Extended unpacking with * ---
first, *middle, last = (1, 2, 3, 4, 5)
print("first:", first, "middle:", middle, "last:", last)

# --- 5. Tuple operations ---
t2 = (76, 77, 42, 6)
t3 = t1 + t2
print("concatenate:", t3)
print("repeat:", t1 * 2)

# --- 6. Unpack in for loop ---
pairs = [(1, "a"), (2, "b"), (3, "c")]
for num, letter in pairs:
    print(num, letter)
