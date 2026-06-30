# 07 — for loop basics
# Run: python 07_for_loop_basics.py
#
# for item in iterable:
#     block
#
# Iterates over each element of a sequence (list, str, tuple, etc.).

# --- 1. Loop over a list ---
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# --- 2. Loop over a string ---
for ch in "Python":
    print(ch, end=" ")
print()

# --- 3. Loop with index using enumerate ---
for index, fruit in enumerate(fruits):
    print(index, fruit)

# --- 4. Loop over a dictionary ---
student = {"name": "Darshan", "city": "Nashik", "age": 25}
for key in student:
    print(key, "->", student[key])

for key, value in student.items():
    print(f"{key}: {value}")

# --- 5. Accumulator pattern (sum) ---
numbers = [10, 20, 30, 40]
total = 0
for n in numbers:
    total += n
print("sum =", total)
