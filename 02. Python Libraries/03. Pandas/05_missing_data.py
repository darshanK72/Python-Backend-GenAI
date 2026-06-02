# 05 — Missing data
# Run: python 05_missing_data.py

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["A", "B", "C", "D"],
    "score": [88, np.nan, 76, 92],
    "attendance": [90, 85, np.nan, 95],
})

print(df)
print("\nisnull:\n", df.isnull())
print("count nulls:\n", df.isnull().sum())

# --- Fill ---
filled = df.fillna({"score": df["score"].mean(), "attendance": 0})
print("\nfilled:\n", filled)

# --- Drop rows with any NaN ---
dropped = df.dropna()
print("\ndropna:\n", dropped)
