# 01 — Matplotlib pyplot basics
# Notebook (recommended): 01-matplotlib.ipynb  (%matplotlib inline)
# Run: python 01_pyplot_basics.py  (saves PNG — no window)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 7, 6]

plt.plot(x, y, marker="o", label="sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Units")
plt.legend()
plt.grid(True, alpha=0.3)

out = "plot_basics.png"
plt.savefig(out, dpi=100, bbox_inches="tight")
plt.close()
print("Saved", out)
os.remove(out)
