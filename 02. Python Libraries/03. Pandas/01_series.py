# 01 — pandas Series
# Notebook (recommended): 01-pandas.ipynb
# Run: python 01_series.py

import pandas as pd

# --- 1. Create Series ---
s = pd.Series([88, 92, 76, 95], index=["Math", "Science", "English", "History"])
print(s)
print("dtype:", s.dtype)

# --- 2. Indexing ---
print("Math:", s["Math"])
print("iloc[0]:", s.iloc[0])

# --- 3. Vectorized ops ---
print("s + 5:\n", s + 5)
print("mean:", s.mean())

# --- 4. From dict ---
temps = pd.Series({"Mon": 32, "Tue": 34, "Wed": 31})
print(temps)
