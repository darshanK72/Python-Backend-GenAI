# 04 — Histograms
# Run: python 04_histogram.py

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

rng = np.random.default_rng(42)
heights = rng.normal(loc=170, scale=8, size=200)

plt.hist(heights, bins=15, color="steelblue", edgecolor="white")
plt.xlabel("Height (cm)")
plt.ylabel("Count")
plt.title("Height Distribution")
plt.savefig("histogram.png")
plt.close()
os.remove("histogram.png")
print("histogram demo OK")
