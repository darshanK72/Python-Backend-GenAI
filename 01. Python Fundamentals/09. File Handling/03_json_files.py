# 03 — JSON files
# Run: python 03_json_files.py

import json
import os

path = "student.json"

student = {
    "name": "Darshan",
    "age": 25,
    "courses": ["Python", "ML"],
    "active": True,
}

# --- 1. Write JSON ---
with open(path, "w", encoding="utf-8") as f:
    json.dump(student, f, indent=2)

# --- 2. Read JSON ---
with open(path, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print("loaded:", loaded)
print("name:", loaded["name"])

# --- 3. String conversion ---
text = json.dumps(student)
back = json.loads(text)
print("round-trip OK:", back == student)

os.remove(path)
