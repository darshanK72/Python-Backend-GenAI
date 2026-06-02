# 16 — Creating dictionaries (fromkeys, zip, comprehensions)
# Run: python 16_dict_creation_patterns.py

# --- 1. Literal ---
d = {"a": 1, "b": 2}

# --- 2. dict() constructor ---
d2 = dict(name="Darshan", city="Nashik")
print("dict():", d2)

# --- 3. fromkeys — same default value for each key ---
keys = ["hello", "world", "python"]
d3 = dict.fromkeys(keys, 0)
print("fromkeys:", d3)

# --- 4. zip — pair two iterables ---
words = ["one", "two", "three"]
nums = [1, 2, 3]
d4 = dict(zip(words, nums))
print("from zip:", d4)

# --- 5. Dict comprehension ---
squares = {x: x ** 2 for x in range(1, 6)}
print("comprehension:", squares)

# --- 6. Count character frequency ---
text = "banana"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print("frequency:", freq)

# --- 7. Nested dictionary ---
student = {
    "name": "Darshan",
    "marks": {"math": 90, "science": 85},
    "hobbies": ["reading", "coding"],
}
print("nested math:", student["marks"]["math"])
print("first hobby:", student["hobbies"][0])
