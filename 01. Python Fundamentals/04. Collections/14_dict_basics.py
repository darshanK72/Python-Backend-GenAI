# 14 — Dictionaries: keys and values
# Run: python 14_dict_basics.py
#
# dict maps unique keys to values. Keys are often strings or numbers.

d1 = {"one": 1, "two": 2, "three": 3}
print("d1:", d1, type(d1))

d2 = {
    "name": "Ravi Sharma",
    "age": 22,
    "marks": 78.23,
    "div": "E",
}

# --- 1. Access by key ---
print("d2['name'] =", d2["name"])
print("d2.get('name') =", d2.get("name"))
print("d2.get('phone') =", d2.get("phone"))           # None if missing
print("d2.get('phone', 'N/A') =", d2.get("phone", "N/A"))

# d2["phone"]   # Uncomment -> KeyError

# --- 2. Add and update ---
d2["address"] = "Nashik"
d2["age"] = 23
print("after updates:", d2)

# --- 3. Length ---
print("len(d2) =", len(d2))

# --- 4. Keys can be many types (but must be hashable) ---
d3 = {
    2: "int key",
    3.14: "float key",
    "str": "string key",
    (1, 2): "tuple key",
}
print("d3:", d3)

# --- 5. Check key exists ---
print("'name' in d2:", "name" in d2)
print("'phone' in d2:", "phone" in d2)
