# 11 — Lambda (small anonymous functions)
# Run: python 11_lambda.py
#
# lambda parameters: expression
# Use for short one-line functions, often with sorted/map/filter.

# --- 1. Basic lambda ---
square = lambda x: x * x
print("square(5) =", square(5))

add = lambda a, b: a + b
print("add(3, 4) =", add(3, 4))

# --- 2. With sorted and a key function ---
students = [
    {"name": "Ravi", "marks": 76},
    {"name": "Meera", "marks": 92},
    {"name": "Asha", "marks": 88},
]
by_marks = sorted(students, key=lambda s: s["marks"], reverse=True)
print("top student:", by_marks[0]["name"])

# --- 3. map and filter ---
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print("squares:", squares)
print("evens:", evens)

# --- 4. When NOT to use lambda ---
# Prefer a normal def when logic is more than one line or needs a docstring.
def is_even(n):
    return n % 2 == 0

print("is_even(4):", is_even(4))
