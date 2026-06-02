# 15 — Practical function examples
# Run: python 15_practical_examples.py

# --- 1. Leap year checker ---
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

for y in [2000, 1900, 2024, 2023]:
    print(y, "leap?", is_leap_year(y))

# --- 2. Temperature converter ---
def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

print("100F =", round(to_celsius(100), 1), "C")

# --- 3. Password strength (simple rules) ---
def is_strong_password(password):
    if len(password) < 8:
        return False
    has_digit = any(ch.isdigit() for ch in password)
    has_alpha = any(ch.isalpha() for ch in password)
    return has_digit and has_alpha

print("strong?", is_strong_password("hello123"))

# --- 4. Average marks ---
def average(*marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)

print("average:", average(78, 85, 92, 88))

# --- 5. Greet with optional title ---
def greet_person(name, title="Mr."):
    return f"Good morning, {title} {name}"

print(greet_person("Sharma"))
print(greet_person("Patel", title="Dr."))
