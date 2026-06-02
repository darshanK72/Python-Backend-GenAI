# 02 — Numbers: int and float
# Run: python 02_numbers.py

# --- 1. int — whole numbers (no size limit in practice for learning) ---
a = 100
b = -7
binary = 0b1010       # 10 in decimal
octal = 0o12          # 10 in decimal
hexadecimal = 0xA     # 10 in decimal
print("int values:", a, b, binary, octal, hexadecimal)

# Underscores make large numbers readable
population = 1_400_000_000
print("population =", population)

# --- 2. float — decimal numbers ---
pi = 3.14
scientific = 1.5e3    # 1.5 * 10^3 = 1500.0
print("pi =", pi, "| scientific =", scientific)

# --- 3. Arithmetic on numbers ---
x, y = 17, 5
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)       # always float division
print("x // y =", x // y)     # floor division (whole number part)
print("x % y =", x % y)       # remainder (modulo)
print("x ** y =", x ** y)     # power

# --- 4. Mixing int and float ---
result = 10 + 2.5
print("10 + 2.5 =", result, type(result))   # result is float

# --- 5. Built-in numeric helpers ---
print("abs(-9) =", abs(-9))
print("round(3.567, 2) =", round(3.567, 2))
print("min(3, 1, 9) =", min(3, 1, 9))
print("max(3, 1, 9) =", max(3, 1, 9))
print("pow(2, 8) =", pow(2, 8))

# --- 6. Float precision quirk (good to know early) ---
print("0.1 + 0.2 =", 0.1 + 0.2)   # not exactly 0.3 due to binary representation
