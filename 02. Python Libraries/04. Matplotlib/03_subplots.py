# 03 — Subplots
# Run: python 03_subplots.py

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import os

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

x = np.linspace(0, 2 * np.pi, 100)
axes[0].plot(x, np.sin(x))
axes[0].set_title("Sine")

axes[1].plot(x, np.cos(x), color="orange")
axes[1].set_title("Cosine")

fig.suptitle("Trig functions")
plt.tight_layout()
plt.savefig("subplots.png")
plt.close()
os.remove("subplots.png")
print("subplots demo OK")
