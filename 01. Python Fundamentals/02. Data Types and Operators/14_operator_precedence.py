# 14 — Operator precedence and associativity
# Run: python 14_operator_precedence.py
#
# When multiple operators appear in one expression, Python follows rules.
# High to low (simplified): **  ->  * / // %  ->  + -  ->  comparisons  ->  not  ->  and  ->  or

# --- 1. Multiplication before addition ---
print("2 + 3 * 4 =", 2 + 3 * 4)        # 14, not 20

# --- 2. Parentheses override everything ---
print("(2 + 3) * 4 =", (2 + 3) * 4)    # 20

# --- 3. Exponent before multiply ---
print("2 ** 3 * 2 =", 2 ** 3 * 2)      # (2**3)*2 = 16

# --- 4. Comparison vs arithmetic ---
print("5 + 3 > 4:", 5 + 3 > 4)

# --- 5. not before and before or ---
print("True or False and False:", True or False and False)   # True
print("not True and False:", not True and False)             # False

# --- 6. Use parentheses when unsure (clearest code) ---
score = 85
passed = (score >= 40) and (score <= 100)
print("passed =", passed)

# --- 7. Assignment has lowest precedence ---
result = 2 + 3 * 4
print("result =", result)
