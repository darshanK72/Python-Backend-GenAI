# 15 — Dictionary methods and iteration
# Run: python 15_dict_methods.py

d2 = {
    "name": "Ravi Sharma",
    "age": 22,
    "marks": 78.23,
    "div": "E",
}

# --- 1. update — merge another dict or key-value pairs ---
d2.update({"school": "K.B.H Vidyalaya", "city": "Nashik"})
print("after update:", d2)

# --- 2. pop — remove key and return value ---
removed = d2.pop("school")
print("popped:", removed, "| d2:", d2)

# --- 3. popitem — remove and return last inserted pair (3.7+ order) ---
key, value = d2.popitem()
print("popitem:", key, value)

# --- 4. keys, values, items ---
print("keys:", list(d2.keys()))
print("values:", list(d2.values()))
print("items:", list(d2.items()))

# --- 5. Looping ---
for key in d2:
    print(key, "->", d2[key])

for key, value in d2.items():
    print(f"{key}: {value}")

for value in d2.values():
    print(value, end=" ")
print()

# --- 6. copy ---
d_copy = d2.copy()
print("copy:", d_copy)

# --- 7. clear ---
temp = {"a": 1}
temp.clear()
print("after clear:", temp)
