# 06 — groupby aggregations
# Run: python 06_groupby.py

import pandas as pd

df = pd.DataFrame({
    "city": ["Nashik", "Pune", "Nashik", "Mumbai", "Pune", "Mumbai"],
    "product": ["A", "A", "B", "A", "B", "B"],
    "sales": [100, 150, 80, 200, 90, 120],
})

# --- 1. Single aggregation ---
by_city = df.groupby("city")["sales"].sum()
print("sum by city:\n", by_city)

# --- 2. Multiple stats ---
stats = df.groupby("city")["sales"].agg(["sum", "mean", "count"])
print("\nstats:\n", stats)

# --- 3. Group by multiple columns ---
multi = df.groupby(["city", "product"])["sales"].sum()
print("\nmulti:\n", multi)
