# 13 — Set operations (math-style)
# Run: python 13_set_operations.py

s1 = {1, 2, 3, 4, 5, 6, 7}
s2 = {4, 5, 6, 7, 8, 9, 10}

# --- 1. union — all elements from both ---
print("union:", s1.union(s2))
print("s1 | s2:", s1 | s2)

# --- 2. intersection — common elements ---
print("intersection:", s1.intersection(s2))
print("s1 & s2:", s1 & s2)

# --- 3. difference — in s1 but not s2 ---
print("difference:", s1.difference(s2))
print("s1 - s2:", s1 - s2)

# --- 4. symmetric_difference — in one but not both ---
print("symmetric:", s1.symmetric_difference(s2))
print("s1 ^ s2:", s1 ^ s2)

# --- 5. In-place updates ---
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print("after intersection_update:", a)

# --- 6. Subset and superset ---
s3 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s4 = {4, 5, 6}
print("s4 subset of s3:", s4.issubset(s3))
print("s3 superset of s4:", s3.issuperset(s4))
print("s4 <= s3:", s4 <= s3)

# --- 7. frozenset — immutable set ---
fs = frozenset([1, 2, 3])
print("frozenset:", fs)
