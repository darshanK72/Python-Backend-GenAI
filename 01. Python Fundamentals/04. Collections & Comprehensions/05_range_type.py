# 05 — range type (often used with for loops)
# Run: python 05_range_type.py
#
# range is not a list — it generates numbers on demand (memory efficient).

# --- 1. Three forms ---
print("range(10):", list(range(10)))
print("range(2, 8):", list(range(2, 8)))
print("range(2, 11, 2):", list(range(2, 11, 2)))

# --- 2. Common patterns ---
print("1..10:", list(range(1, 11)))
print("evens 2-20:", list(range(2, 21, 2)))
print("countdown:", list(range(5, 0, -1)))

# --- 3. Use in for loop ---
for i in range(3):
    print("i =", i)

# --- 4. range object properties ---
r = range(5, 15, 2)
print("start:", r.start, "stop:", r.stop, "step:", r.step)
print("len(range(5,15,2)) =", len(r))
print("5 in range(5,15,2):", 5 in r)

# --- 5. Convert to list when you need all values at once ---
print(list(range(2, 31)))
