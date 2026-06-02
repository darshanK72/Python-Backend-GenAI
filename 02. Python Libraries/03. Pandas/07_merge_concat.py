# 07 — merge and concat
# Run: python 07_merge_concat.py

import pandas as pd

students = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Asha", "Ravi", "Meera"],
})
marks = pd.DataFrame({
    "id": [1, 2, 4],
    "math": [90, 76, 88],
})

# --- 1. merge (SQL-style join) ---
inner = pd.merge(students, marks, on="id", how="inner")
left = pd.merge(students, marks, on="id", how="left")
print("inner:\n", inner)
print("left:\n", left)

# --- 2. concat rows ---
q1 = pd.DataFrame({"month": ["Jan", "Feb"], "sales": [100, 120]})
q2 = pd.DataFrame({"month": ["Mar", "Apr"], "sales": [140, 130]})
year = pd.concat([q1, q2], ignore_index=True)
print("\nconcat:\n", year)
