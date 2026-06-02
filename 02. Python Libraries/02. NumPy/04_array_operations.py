# 04 — NumPy array operations
# Run: python 04_array_operations.py

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print("a + b =", a + b)
print("a * b =", a * b)
print("dot =", np.dot(a, b))

# --- 2. Universal functions ---
print("sqrt:", np.sqrt(a))
print("exp:", np.exp(a))
print("mean:", np.mean(a))

# --- 3. 2D operations ---
m = np.array([[1, 2], [3, 4]])
print("sum all:", m.sum())
print("sum axis=0:", m.sum(axis=0))
print("sum axis=1:", m.sum(axis=1))

# --- 4. Reshape ---
flat = np.arange(12)
grid = flat.reshape(3, 4)
print("grid:\n", grid)
print("flatten:", grid.ravel())
