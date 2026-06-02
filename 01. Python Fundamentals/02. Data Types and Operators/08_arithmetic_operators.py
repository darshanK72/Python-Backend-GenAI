# 08 — Arithmetic operators
# Run: python 08_arithmetic_operators.py
#
# +  -  *  /  //  %  **

a, b = 52, 14

# --- 1. Basic operators ---
print("a + b =", a + b)     # addition
print("a - b =", a - b)     # subtraction
print("a * b =", a * b)     # multiplication
print("a / b =", a / b)     # true division (float result)
print("a // b =", a // b)   # floor division
print("a % b =", a % b)     # remainder
print("4 ** 2 =", 4 ** 2)   # exponent

# --- 2. Negative and unary plus ---
print("-a =", -a)
print("+a =", +a)

# --- 3. Strings and lists support + and * ---
print("hello" + " world")
print([1, 2] + [3, 4])
print("ha" * 3)

# --- 4. Modulo use cases ---
print("17 % 5 =", 17 % 5)           # remainder
print("even?", 10 % 2 == 0)         # check even
print("last digit of 1234:", 1234 % 10)

# --- 5. Floor division with negatives (rounds toward negative infinity) ---
print("-7 // 2 =", -7 // 2)
print("-7 / 2 =", -7 / 2)
