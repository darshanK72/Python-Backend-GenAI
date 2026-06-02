# 01 — NumPy introduction
# Notebook (recommended): 01-numpy.ipynb
# Run: python 01_numpy_intro.py

import numpy as np

print("NumPy version:", np.__version__)

# --- 1. Why NumPy? Fast array math in C ---
# Lists of numbers are slow for large math; ndarray is optimized.

py_list = [1, 2, 3, 4, 5]
arr = np.array(py_list)
print("array:", arr)
print("type:", type(arr))
print("dtype:", arr.dtype)

# --- 2. Vectorized operations (no explicit loop) ---
print("arr * 2 =", arr * 2)
print("arr ** 2 =", arr ** 2)
print("sum =", arr.sum())

# --- 3. Common dtypes ---
print(np.array([1, 2, 3], dtype=np.int32))
print(np.array([1.5, 2.5], dtype=np.float64))
