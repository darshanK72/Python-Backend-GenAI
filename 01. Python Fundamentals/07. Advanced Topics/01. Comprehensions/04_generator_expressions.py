# 04 — Generator expressions (lazy comprehension)
# Run: python 04_generator_expressions.py
#
# (expr for item in iterable) — like list comp but yields one item at a time.
# Saves memory for large sequences.

# --- 1. List comp vs generator ---
list_comp = [x ** 2 for x in range(5)]
gen_exp = (x ** 2 for x in range(5))

print("list:", list_comp, type(list_comp))
print("generator:", gen_exp, type(gen_exp))

# --- 2. Consume generator ---
print("values:", list(gen_exp))

# --- 3. sum() works without building full list ---
total = sum(x ** 2 for x in range(1000000))
print("sum of squares (first 1M):", total)

# --- 4. any / all with generator ---
has_big = any(n > 90 for n in [45, 67, 92, 33])
print("has_big:", has_big)

# --- 5. Generator is one-shot ---
g = (n for n in range(3))
print(list(g))
print(list(g))   # [] — already exhausted
