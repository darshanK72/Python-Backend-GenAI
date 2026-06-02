# 09 — Assignment operators
# Run: python 09_assignment_operators.py
#
# = assigns; combined forms update the variable in place.

x = 20
print("x =", x)

# --- 1. Compound assignment ---
x += 5      # same as x = x + 5
print("after x += 5:", x)

x -= 10
print("after x -= 10:", x)

x *= 3
print("after x *= 3:", x)

x /= 4
print("after x /= 4:", x)

x //= 2
print("after x //= 2:", x)

x %= 3
print("after x %= 3:", x)

x **= 4
print("after x **= 4:", x)

# --- 2. On strings and lists ---
s = "Py"
s += "thon"
print("s =", s)

nums = [1, 2]
nums += [3, 4]
print("nums =", nums)

# --- 3. Multiple assignment (unpacking) ---
a, b, c = 1, 2, 3
print(a, b, c)

# swap without temp variable
a, b = b, a
print("swapped:", a, b)

# --- 4. Walrus operator := (assign inside expression, Python 3.8+) ---
# n = len(data) can be written as (n := len(data)) in an expression
data = [10, 20, 30]
if (length := len(data)) > 2:
    print("data has", length, "items")
