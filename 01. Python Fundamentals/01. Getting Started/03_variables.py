# 03 — Variables and basic data types
# Run: python 03_variables.py
#
# A variable is a name that refers to a value in memory.
# You assign with =  (read as: "name gets value", not "equals").
# Python is dynamically typed: the same name can later hold a different type.

# --- 1. Integer (int) — whole numbers ---
a = 50
print("a =", a, "| type:", type(a))

# --- 2. Float (float) — numbers with a decimal point ---
b = 534.63
print("b =", b, "| type:", type(b))

# --- 3. Complex (complex) — real + imaginary part (uses j, not i) ---
c = 4 + 3j
print("c =", c, "| type:", type(c))

# --- 4. String (str) — text in quotes ---
s = "hello World"
print("s =", s, "| type:", type(s))

single_char = "T"   # one character is still a str, not a separate "char" type
print("single_char =", single_char, "| type:", type(single_char))

# --- 5. Boolean (bool) — only True or False (capital T and F) ---
is_active = True
print("is_active =", is_active, "| type:", type(is_active))

# --- 6. None — means "no value" / empty placeholder ---
result = None
print("result =", result, "| type:", type(result))

# --- 7. Reassigning a variable (value can change) ---
count = 1
print("count =", count)
count = count + 1
print("after count = count + 1 ->", count)

# Same name can even point to a different type later:
box = 100
print("box as int:", box, type(box))
box = "now text"
print("box as str:", box, type(box))

# --- 8. Names are case-sensitive ---
hello = 2303
HELLO = 6345          # hello and HELLO are two different variables
print("hello =", hello, "| HELLO =", HELLO)

# --- 9. Assign one value to many names ---
x = y = z = 100
print("x, y, z =", x, y, z)

# --- 10. Assign multiple values in one line (unpacking) ---
p, q, r = 60, 45, 90
print("p, q, r =", p, q, r)

# --- 11. Delete a variable with del ---
temp = "can be removed"
del temp
# print(temp)  # Uncomment → NameError: name 'temp' is not defined
print("Variable temp was deleted with del.")
