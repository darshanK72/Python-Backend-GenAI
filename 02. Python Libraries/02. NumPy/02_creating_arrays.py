# 02 — Creating NumPy arrays
# Run: python 02_creating_arrays.py

import numpy as np

# --- 1. From Python sequences ---
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
print("1D:", a.shape)
print("2D:\n", b)

# --- 2. zeros, ones, full ---
print("zeros:\n", np.zeros((2, 3)))
print("ones:\n", np.ones((3, 2)))
print("full:\n", np.full((2, 2), 7))

# --- 3. arange and linspace ---
print("arange:", np.arange(0, 10, 2))
print("linspace:", np.linspace(0, 1, 5))

# --- 4. Identity matrix ---
print("eye:\n", np.eye(3))

# --- 5. Random ---
rng = np.random.default_rng(42)
print("integers:", rng.integers(1, 7, size=5))
print("uniform:", rng.random(3))
