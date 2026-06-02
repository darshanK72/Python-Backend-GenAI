# 14 — Useful built-ins with functions
# Run: python 14_builtin_and_helpers.py

nums = [3, 1, 4, 1, 5, 9]

# --- 1. Common built-ins ---
print("len:", len(nums))
print("sum:", sum(nums))
print("min/max:", min(nums), max(nums))
print("sorted:", sorted(nums))

# --- 2. type checking helpers ---
print("isinstance(5, int):", isinstance(5, int))
print("callable(print):", callable(print))

# --- 3. all / any ---
print("all positive:", all(n > 0 for n in nums))
print("any even:", any(n % 2 == 0 for n in nums))

# --- 4. enumerate and zip in loops ---
names = ["A", "B", "C"]
for i, name in enumerate(names):
    print(i, name)

for name, score in zip(names, [90, 85, 88]):
    print(name, score)

# --- 5. map / filter as alternatives to loops ---
doubled = list(map(lambda x: x * 2, nums))
big = list(filter(lambda x: x > 3, nums))
print("doubled:", doubled)
print("big:", big)
