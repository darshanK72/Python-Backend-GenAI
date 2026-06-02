# 07 — NumPy linear algebra (intro)
# Run: python 07_linear_algebra_intro.py

import numpy as np

A = np.array([[2, 1], [1, 3]])
B = np.array([[1, 0], [2, 1]])

print("matrix multiply:\n", A @ B)

# --- Solve Ax = b ---
b = np.array([5, 7])
x = np.linalg.solve(A, b)
print("solution x:", x)
print("check:", A @ x)

# --- Determinant and inverse ---
print("det:", np.linalg.det(A))
print("inverse:\n", np.linalg.inv(A))
