# 03 — if, elif, else (multiple branches)
# Run: python 03_if_elif_else.py
#
# elif = "else if" — check the next condition only if previous ones were False.

# --- 1. Greatest of three numbers ---
x, y, z = 45, 78, 62

if x > y and x > z:
    print("Largest is x =", x)
elif y > x and y > z:
    print("Largest is y =", y)
else:
    print("Largest is z =", z)

# --- 2. Grade bands ---
marks = 76

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")

# --- 3. elif is optional; you can have if / elif without else ---
temperature = -5
if temperature > 30:
    print("Hot")
elif temperature > 10:
    print("Mild")
elif temperature > 0:
    print("Cold")

# --- 4. Only ONE branch runs (first True condition wins) ---
n = 15
if n > 20:
    print("big")
elif n > 10:
    print("medium")   # this runs
elif n > 5:
    print("small")    # skipped even though n > 5 is True
