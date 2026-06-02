# 04 — User input with input()
# Run: python 04_input.py
#
# input(prompt) shows prompt text, waits for you to type, then press Enter.
# IMPORTANT: input() ALWAYS returns a str (string) — even if you type digits.

# --- 1. Reading text ---
name = input("Enter your name: ")
print("Welcome,", name)
print("type(name) =", type(name))

# --- 2. Stripping extra spaces ---
# Users often add spaces by mistake. .strip() removes leading/trailing spaces.
city = input("Enter your city: ").strip()
print("City:", city)

# --- 3. Converting to int (whole number) ---
# Wrap input() with int() before doing math.
age = int(input("Enter your age: "))
print("Next year you will be", age + 1)
print("type(age) =", type(age))

# --- 4. Converting to float (decimal number) ---
marks = float(input("Enter your marks: "))
print("Marks:", marks)
print("type(marks) =", type(marks))

# --- 5. Converting to complex ---
# Format example: 3+4j  (no spaces around + is safest for beginners)
comp = complex(input("Enter a complex number (e.g. 3+4j): "))
print("Complex number:", comp)
print("type(comp) =", type(comp))

# --- 6. Reading two numbers from one line ---
# "10 20".split() → ["10", "20"]
line = input("Enter two whole numbers separated by space (e.g. 10 20): ")
first, second = line.split()
print("Sum =", int(first) + int(second))

# If conversion fails (e.g. typing letters), Python raises ValueError.
# Example: int("hello")  # ValueError
