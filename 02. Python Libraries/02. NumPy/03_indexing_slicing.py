# 03 — NumPy indexing and slicing
# Run: python 03_indexing_slicing.py

import numpy as np

arr = np.arange(10, 20)
print("arr:", arr)
print("arr[2:7]:", arr[2:7])
print("arr[-3:]:", arr[-3:])
print("arr[::2]:", arr[::2])

# --- 2D ---
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("m[1, 2] =", m[1, 2])
print("row 0:", m[0])
print("col 1:", m[:, 1])
print("submatrix:\n", m[0:2, 1:3])

# --- Boolean indexing ---
nums = np.array([12, 5, 8, 21, 4])
print("evens:", nums[nums % 2 == 0])
print("greater than 10:", nums[nums > 10])
