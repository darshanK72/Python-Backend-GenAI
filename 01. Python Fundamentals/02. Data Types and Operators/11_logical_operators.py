# 11 — Logical operators: and, or, not
# Run: python 11_logical_operators.py

a, b, c = 52, 14, 67

# --- 1. and — True only if BOTH sides are True ---
ra = (a > b) and (a > c)
rb = (b > a) and (b > c)
rc = (c > a) and (c > b)
print("ra =", ra, "| rb =", rb, "| rc =", rc)

# --- 2. or — True if AT LEAST one side is True ---
print("(a > 100) or (b < 20):", (a > 100) or (b < 20))

# --- 3. not — flips True/False ---
print("not (a > b):", not (a > b))

# --- 4. Short-circuit evaluation ---
# If first part of "and" is False, second part is not evaluated.
def side_effect():
    print("  side_effect() ran")
    return True

print("False and side_effect():")
result = False and side_effect()   # side_effect never runs
print("result =", result)

print("True and side_effect():")
result = True and side_effect()

# --- 5. Combining with comparisons ---
marks = 85
attendance = 90
print("pass?", marks >= 40 and attendance >= 75)

# --- 6. Truthiness in conditions (no need to write == True) ---
name = "Darshan"
if name:          # non-empty string is truthy
    print("name is set")
