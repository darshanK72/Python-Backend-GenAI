# 01 — Seaborn (statistical plots on Matplotlib)
# Notebook (recommended): 01-seaborn.ipynb
# Run: python 01_seaborn_intro.py  (saves PNG)

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

df = pd.DataFrame({
    "hours": [1, 2, 3, 4, 5, 2, 3, 4, 5, 6],
    "score": [55, 60, 65, 70, 80, 58, 68, 72, 85, 90],
    "course": ["A"] * 5 + ["B"] * 5,
})

sns.set_theme(style="whitegrid")
sns.scatterplot(data=df, x="hours", y="score", hue="course")
plt.title("Study hours vs score")
plt.savefig("seaborn_scatter.png")
plt.close()
os.remove("seaborn_scatter.png")
print("seaborn scatter OK")
