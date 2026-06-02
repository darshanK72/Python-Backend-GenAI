# 03 — Heatmap (correlation matrix)
# Run: python 03_heatmap.py

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

df = pd.DataFrame({
    "math": [90, 76, 88, 95],
    "science": [85, 70, 92, 90],
    "english": [88, 82, 80, 93],
    "attendance": [95, 60, 90, 98],
})

corr = df.corr()
plt.figure(figsize=(5, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation heatmap")
plt.savefig("heatmap.png")
plt.close()
os.remove("heatmap.png")
print("heatmap OK")
