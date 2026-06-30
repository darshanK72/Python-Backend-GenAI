# 01 — Collections overview
# Run: python 01_collections_overview.py
#
# Python's main built-in collections store multiple values.
# str, list, tuple = sequences (ordered, indexable)
# set = unordered unique items
# dict = key-value pairs (insertion-ordered since Python 3.7)

# --- 1. String (str) — text, immutable sequence ---
s = "hello"
print("str:", s, type(s))

# --- 2. List — ordered, mutable, allows duplicates ---
nums = [10, 20, 30, 20]
print("list:", nums, type(nums))

# --- 3. Tuple — ordered, immutable ---
point = (10, 20)
print("tuple:", point, type(point))

# --- 4. Set — unordered, unique elements, mutable ---
tags = {"python", "code", "python"}
print("set:", tags, type(tags))

# --- 5. Dictionary — keys map to values ---
user = {"name": "Darshan", "city": "Nashik"}
print("dict:", user, type(user))

# --- 6. Quick comparison ---
print("\nMutable:   list, set, dict")
print("Immutable: str, tuple, frozenset (intro later)")
print("Ordered:   str, list, tuple, dict (3.7+)")
print("Indexed:   str, list, tuple (by integer position)")
