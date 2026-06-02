# 02 — Seaborn distribution plots
# Run: python 02_distribution_plots.py

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

rng = np.random.default_rng(0)
df = pd.DataFrame({
    "value": rng.normal(100, 15, 80),
    "group": ["A"] * 40 + ["B"] * 40,
})

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
sns.histplot(data=df, x="value", hue="group", ax=axes[0], kde=True)
sns.boxplot(data=df, x="group", y="value", ax=axes[1])
plt.tight_layout()
plt.savefig("seaborn_dist.png")
plt.close()
os.remove("seaborn_dist.png")
print("distribution plots OK")
