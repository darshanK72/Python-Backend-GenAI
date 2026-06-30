# 02 — Dict and set comprehension
# Run: python 02_dict_set_comprehension.py

# --- 1. Dict comprehension: {key_expr: value_expr for ...} ---
squares_dict = {i: i * i for i in range(1, 11)}
print("squares_dict:", squares_dict)

# --- 2. Swap keys and values ---
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print("swapped:", swapped)

# --- 3. Filter while building ---
scores = {"math": 88, "science": 42, "english": 76}
passed = {k: v for k, v in scores.items() if v >= 50}
print("passed:", passed)

# --- 4. Set comprehension: {expr for ...} ---
nums = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {n ** 2 for n in nums}
print("unique_squares:", unique_squares)

# --- 5. Remove vowels from a word ---
word = "comprehension"
consonants = {ch for ch in word if ch not in "aeiou"}
print("consonants:", consonants)
