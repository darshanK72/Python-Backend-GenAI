# 10 — Comparison operators (return True or False)
# Run: python 10_comparison_operators.py
#
# ==  !=  >  <  >=  <=

a, b = 52, 14

print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# --- 1. Chained comparisons (readable math style) ---
age = 25
print("18 <= age <= 60:", 18 <= age <= 60)

# --- 2. Comparing strings (lexicographic / dictionary order) ---
print("'apple' < 'banana':", "apple" < "banana")
print("'Z' < 'a':", "Z" < "a")   # uppercase before lowercase in ASCII

# --- 3. == vs is ---
x = [1, 2]
y = [1, 2]
print("x == y:", x == y)     # same content
print("x is y:", x is y)     # same object in memory? False

# --- 4. None checks ---
value = None
print("value is None:", value is None)
print("value == None:", value == None)   # works but "is None" is preferred
