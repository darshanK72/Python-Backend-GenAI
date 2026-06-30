# 17 — Nested collections (list of dicts, dict of lists, etc.)
# Run: python 17_nested_collections.py

# --- 1. List of dictionaries (common for records) ---
students = [
    {"name": "Asha", "marks": 88},
    {"name": "Ravi", "marks": 76},
    {"name": "Meera", "marks": 92},
]

for s in students:
    print(s["name"], s["marks"])

# --- 2. Dictionary of lists ---
groups = {
    "fruits": ["apple", "banana"],
    "colors": ["red", "green", "blue"],
}
groups["fruits"].append("cherry")
print("groups:", groups)

# --- 3. Matrix as list of lists ---
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print("matrix[1][2] =", matrix[1][2])

for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

# --- 4. Tuple inside dict (immutable nested record) ---
config = {
    "size": (1920, 1080),
    "enabled": True,
}
print("resolution:", config["size"][0], "x", config["size"][1])
