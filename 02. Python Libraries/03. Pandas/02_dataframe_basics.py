# 02 — DataFrame basics
# Run: python 02_dataframe_basics.py

import pandas as pd

data = {
    "name": ["Asha", "Ravi", "Meera", "Kiran"],
    "age": [22, 23, 21, 24],
    "city": ["Nashik", "Pune", "Mumbai", "Nashik"],
    "score": [88, 76, 92, 85],
}
df = pd.DataFrame(data)
print(df)
print("\nshape:", df.shape)
print("columns:", list(df.columns))
print("dtypes:\n", df.dtypes)

# --- Quick stats ---
print("\n", df.describe())
