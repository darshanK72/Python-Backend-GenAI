# 06 — Lists: create, access, modify
# Run: python 06_list_basics.py
#
# Lists are ordered, mutable, and can hold mixed types.

l = [4, 52, 25, 3, 62]
l1 = [1, 42, 56.35, "hello", True, (3 + 4j), [76, 634]]

# --- 1. Access by index ---
print("l1[0] =", l1[0])
print("l1[-3] =", l1[-3])
print("nested:", l1[-1][1])

# --- 2. Change items (mutable) ---
l1[0] = 1000
print("after l1[0] = 1000:", l1[0])

# --- 3. Slicing ---
print("l1[:5] =", l1[:5])
print("l1[2:6] =", l1[2:6])
print("l1[2:10:2] =", l1[2:10:2])
print("reverse:", l1[::-1])

# --- 4. Iterate ---
for i in range(len(l1)):
    print(l1[i], end=" ")
print()

for item in l1:
    print(item, end=" ")
print()

# --- 5. Operators ---
print("l * 2 =", l * 2)
print("l + [99] =", l + [99])

# --- 6. Create lists ---
empty = []
from_range = list(range(5))
print("from_range:", from_range)
