# 08 — sort, apply, value_counts
# Run: python 08_sort_apply.py

import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meera", "Kiran"],
    "score": [88, 76, 92, 85],
    "grade": ["B", "C", "A", "B"],
})

# --- 1. Sort ---
print(df.sort_values("score", ascending=False))

# --- 2. apply on column ---
df["passed"] = df["score"].apply(lambda x: x >= 40)
print(df)

# --- 3. value_counts ---
print(df["grade"].value_counts())

# --- 4. Rename columns ---
renamed = df.rename(columns={"name": "student_name"})
print(renamed.columns.tolist())
