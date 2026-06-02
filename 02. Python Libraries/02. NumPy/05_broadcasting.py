# 05 — Broadcasting
# Run: python 05_broadcasting.py
#
# NumPy stretches smaller arrays to match shapes for element-wise ops.

import numpy as np

# --- 1. Scalar + array ---
arr = np.array([1, 2, 3, 4])
print(arr + 10)

# --- 2. Row + column ---
matrix = np.arange(12).reshape(3, 4)
col = np.array([[10], [20], [30]])
print("matrix + col:\n", matrix + col)

# --- 3. Normalize rows (subtract mean per row) ---
data = np.array([[1, 2, 3], [10, 20, 30], [100, 200, 300]], dtype=float)
means = data.mean(axis=1, keepdims=True)
normalized = data - means
print("normalized:\n", normalized)
