# 06 — Collections preview (full lessons in folder 05)
# Run: python 06_collections_preview.py
#
# Quick look at list, tuple, set, dict — enough to recognize types and operators.

# --- 1. list — ordered, changeable, allows duplicates ---
fruits = ["apple", "banana", "apple"]
fruits.append("cherry")
print("list:", fruits, type(fruits))

# --- 2. tuple — ordered, unchangeable ---
point = (10, 20)
print("tuple:", point, type(point))
# point[0] = 5   # Uncomment -> TypeError

# --- 3. set — unordered, no duplicates ---
tags = {"python", "code", "python"}
print("set:", tags, type(tags))

# --- 4. dict — key-value pairs ---
user = {"name": "Darshan", "city": "Nashik"}
user["age"] = 25
print("dict:", user, type(user))

# --- 5. len() works on sequences and collections ---
print("len(fruits) =", len(fruits))
print("len(user) =", len(user))

# --- 6. Checking type with isinstance (better than type() alone) ---
print("isinstance(fruits, list) =", isinstance(fruits, list))
print("isinstance(point, tuple) =", isinstance(point, tuple))
