# 06 — f-strings (formatted string literals)
# Run: python 06_f_strings.py
#
# Put f or F before the opening quote: f"..."
# Inside { ... } you can place variables and expressions.
# Preferred in modern Python for readable output.

name = "Darshan"
age = 25
marks = 88.5

# --- 1. Basic embedding ---
print(f"Hello, {name}!")
print(f"Next year you will be {age + 1}")
print(f"Marks: {marks}")

# --- 2. Any expression inside braces ---
print(f"Type of age: {type(age)}")
print(f"Passed? {marks >= 40}")

# --- 3. Format numbers ---
pi = 3.14159265
print(f"Pi to 2 decimals: {pi:.2f}")      # .2f = float with 2 decimal places
print(f"Large number: {1_000_000:,}")     # :, = thousands separator

# --- 4. Alignment and padding (useful for tables) ---
label = "Score"
print(f"{label:>10}: {marks}")            # >10 = right-align in width 10

# --- 5. Multiple values in one f-string ---
a, b = 10, 3
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")

# --- 6. Quotes inside f-strings ---
word = "Python"
print(f"I am learning {word!r}")          # !r shows quotes around string (repr style)

# --- 7. Literal curly braces ---
# Use {{ and }} to print actual { } characters
print(f"Set notation example: {{x | x > 0}}")

# --- 8. f-string vs older style (know it exists) ---
print("Hello, {}!".format(name))          # .format — older, still common in legacy code
