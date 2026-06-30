# 13 — Common loop patterns
# Run: python 13_loop_patterns.py

# --- 1. Sum of numbers 1 to n ---
n = 10
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum 1..{n} =", total)

# --- 2. Count how many match a condition ---
numbers = [12, 5, 8, 21, 4, 16]
evens = 0
for num in numbers:
    if num % 2 == 0:
        evens += 1
print("Even count:", evens)

# --- 3. Find maximum ---
data = [45, 12, 78, 3, 56]
maximum = data[0]
for value in data[1:]:
    if value > maximum:
        maximum = value
print("max =", maximum)

# --- 4. Build a new list ---
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print("squares =", squares)

# --- 5. Menu loop pattern (simulated) ---
choices = ["add", "add", "quit"]
for action in choices:
    if action == "quit":
        print("Exiting menu")
        break
    print("Doing:", action)
