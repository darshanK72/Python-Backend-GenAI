# 02 — Bar charts and scatter plots
# Run: python 02_bar_and_scatter.py

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

# --- Bar ---
categories = ["Python", "SQL", "ML", "Cloud"]
values = [90, 75, 60, 45]
plt.figure(figsize=(6, 4))
plt.bar(categories, values, color=["#4C72B0", "#55A868", "#C44E52", "#8172B2"])
plt.title("Skill Scores")
plt.ylabel("Score")
plt.savefig("bar_chart.png")
plt.close()

# --- Scatter ---
hours = [1, 2, 3, 4, 5, 6]
scores = [55, 62, 68, 74, 80, 88]
plt.figure()
plt.scatter(hours, scores, s=80, c="teal", alpha=0.8)
plt.xlabel("Study hours")
plt.ylabel("Exam score")
plt.title("Study vs Score")
plt.savefig("scatter_chart.png")
plt.close()

for f in ["bar_chart.png", "scatter_chart.png"]:
    os.remove(f)
print("Charts saved and removed (demo)")
