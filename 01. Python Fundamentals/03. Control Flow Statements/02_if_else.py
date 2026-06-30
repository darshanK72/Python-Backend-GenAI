# 02 — if and else
# Run: python 02_if_else.py
#
# Syntax:
#   if condition:
#       block
#   else:
#       block

a, b = 52, 14

# --- 1. Simple if ---
if a > b:
    print("a is greater than b")

# --- 2. if-else ---
if a > b:
    print("greater:", a)
else:
    print("greater:", b)

# --- 3. Condition can be any expression that is True or False ---
age = 17
if age >= 18:
    print("Adult")
else:
    print("Minor")

# --- 4. No parentheses required (optional style) ---
if (a % 2) == 0:
    print(a, "is even")
else:
    print(a, "is odd")

# --- 5. Multiple statements in a block (same indent) ---
marks = 92
if marks >= 90:
    grade = "A"
    message = "Excellent"
    print(grade, "-", message)
