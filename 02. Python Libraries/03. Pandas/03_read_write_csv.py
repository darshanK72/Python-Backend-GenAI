# 03 — Read and write CSV
# Run: python 03_read_write_csv.py

import pandas as pd
import os

df = pd.DataFrame({
    "product": ["Pen", "Notebook", "Bag"],
    "price": [20, 120, 800],
    "stock": [100, 50, 15],
})

path = "products.csv"
df.to_csv(path, index=False)
print("wrote", path)

loaded = pd.read_csv(path)
print("loaded:\n", loaded)

# --- Options ---
# pd.read_csv("file.csv", usecols=["a", "b"], nrows=1000)
# df.to_csv("out.csv", index=False, encoding="utf-8")

os.remove(path)
