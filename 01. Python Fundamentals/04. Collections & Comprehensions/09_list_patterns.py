# 09 — Common list patterns
# Run: python 09_list_patterns.py

# --- 1. Build a list in a loop ---
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print("squares:", squares)

# --- 2. Filter evens ---
nums = [12, 5, 8, 21, 4, 16]
evens = []
for n in nums:
    if n % 2 == 0:
        evens.append(n)
print("evens:", evens)

# --- 3. List comprehension (preview; full lesson in Advanced Topics) ---
squares2 = [x ** 2 for x in range(1, 6)]
evens2 = [n for n in nums if n % 2 == 0]
print("comprehension squares:", squares2)
print("comprehension evens:", evens2)

# --- 4. Enumerate with index ---
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)

# --- 5. zip two lists ---
names = ["A", "B", "C"]
scores = [90, 85, 88]
for name, score in zip(names, scores):
    print(name, score)
