# 04 — Selecting and filtering rows
# Run: python 04_selection_filtering.py

import pandas as pd

df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Meera", "Kiran"],
    "dept": ["IT", "HR", "IT", "Finance"],
    "salary": [60000, 45000, 62000, 55000],
})

# --- 1. Columns ---
print(df["name"])
print(df[["name", "salary"]])

# --- 2. loc (by label) ---
print(df.loc[0:2, ["name", "dept"]])

# --- 3. iloc (by position) ---
print(df.iloc[1:3, 0:2])

# --- 4. Boolean filter ---
high = df[df["salary"] > 50000]
print("salary > 50000:\n", high)

it_dept = df[(df["dept"] == "IT") & (df["salary"] > 55000)]
print("IT and high pay:\n", it_dept)
