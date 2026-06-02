# 05 — Type casting (explicit conversion between types)
# Run: python 05_typecasting.py
#
# Casting = calling int(), float(), str(), bool(), etc. to build a new value.
# Use it when types do not match (e.g. input gives str, you need int for math).

x = 42
print("x =", x, "| type:", type(x))

# --- 1. int → float ---
y = float(x)
print("float(42) =", y, "| type:", type(y))

# --- 2. float → int (truncates — cuts off decimal, does NOT round) ---
z = int(6445.99)
print("int(6445.99) =", z, "| type:", type(z))

# Use round() when you want normal rounding:
print("round(6445.99) =", round(6445.99))

# --- 3. int → complex ---
p = complex(3)
print("complex(3) =", p, "| type:", type(p))

# --- 4. number → string ---
a = str(345345)
print("str(345345) =", a, "| type:", type(a))
print("Can concatenate:", "ID-" + a)

# --- 5. string → int ---
b = int("536745")
print('int("536745") =', b, "| type:", type(b))

# --- 6. string → float ---
c = float("634.74")
print('float("634.74") =', c, "| type:", type(c))

# --- 7. bool casting ---
# Falsy → False: 0, 0.0, "", None, empty collections (later)
# Most other values → True
print("bool(0) =", bool(0))
print("bool(1) =", bool(1))
print('bool("") =', bool(""))
print('bool("hi") =', bool("hi"))

# --- 8. bool → int / str ---
print("int(True) =", int(True), "| int(False) =", int(False))
print("str(True) =", str(True))

# --- 9. Invalid conversion raises ValueError ---
# int("hello")   # ValueError: invalid literal for int()
print("Uncomment int(\"hello\") above to see ValueError.")
