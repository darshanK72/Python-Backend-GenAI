# 04 — CSV files
# Run: python 04_csv_files.py

import csv
import os

path = "scores.csv"
rows = [
    ["name", "subject", "score"],
    ["Asha", "Math", "90"],
    ["Ravi", "Math", "76"],
    ["Meera", "Science", "88"],
]

# --- 1. Write CSV ---
with open(path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

# --- 2. Read CSV ---
print("--- rows ---")
with open(path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# --- 3. DictReader / DictWriter ---
with open(path, "r", encoding="utf-8") as f:
    dict_reader = csv.DictReader(f)
    for record in dict_reader:
        print(record["name"], record["score"])

os.remove(path)
