# 08 — Save and load NumPy arrays
# Run: python 08_save_load.py

import numpy as np
import os

arr = np.arange(1, 13).reshape(3, 4)

# --- 1. Binary .npy ---
np.save("demo_array.npy", arr)
loaded = np.load("demo_array.npy")
print("loaded:\n", loaded)

# --- 2. Multiple arrays .npz ---
np.savez("demo_bundle.npz", data=arr, meta=np.array([2026, 6, 2]))
with np.load("demo_bundle.npz") as bundle:
    print("keys:", bundle.files)
    print("data:\n", bundle["data"])

# --- 3. Text (small arrays) ---
np.savetxt("demo_array.txt", arr, fmt="%d")
text_loaded = np.loadtxt("demo_array.txt")
print("from txt:\n", text_loaded)

for f in ["demo_array.npy", "demo_bundle.npz", "demo_array.txt"]:
    os.remove(f)
print("cleanup done")
