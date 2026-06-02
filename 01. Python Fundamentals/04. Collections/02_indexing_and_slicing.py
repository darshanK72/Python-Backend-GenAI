# 02 — Indexing and slicing (shared by str, list, tuple)
# Run: python 02_indexing_and_slicing.py
#
# Index: position of an item. First = 0, last = -1.
# Slice: [start:stop:step] — stop is exclusive.

data = [10, 20, 30, 40, 50, 60]

# --- 1. Positive indexing ---
print("data[0] =", data[0])
print("data[3] =", data[3])

# --- 2. Negative indexing (from the end) ---
print("data[-1] =", data[-1])
print("data[-2] =", data[-2])

# --- 3. Slicing ---
print("data[1:4] =", data[1:4])      # index 1,2,3
print("data[:3] =", data[:3])        # from start
print("data[3:] =", data[3:])        # to end
print("data[:] =", data[:])          # full copy (shallow)
print("data[::2] =", data[::2])      # every 2nd item
print("data[::-1] =", data[::-1])    # reverse

# --- 4. Same rules on strings ---
word = "Python"
print("word[0] =", word[0])
print("word[2:5] =", word[2:5])
print("reverse =", word[::-1])

# --- 5. len() ---
print("len(data) =", len(data))

# --- 6. IndexError ---
# print(data[100])   # Uncomment -> IndexError
