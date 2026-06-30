# 04 — itertools module (iterator tools)
# Run: python 04_itertools_intro.py

import itertools

# --- 1. infinite iterators ---
counter = itertools.count(10, 2)
print("count:", [next(counter) for _ in range(5)])

# --- 2. cycle and repeat ---
print("cycle:", list(itertools.islice(itertools.cycle("AB"), 7)))
print("repeat:", list(itertools.repeat(7, 4)))

# --- 3. combinators ---
print("chain:", list(itertools.chain([1, 2], [3, 4])))
print("zip_longest:", list(itertools.zip_longest([1, 2], [10, 20, 30], fillvalue=0)))

# --- 4. combinations / permutations ---
print("combinations:", list(itertools.combinations("ABC", 2)))
print("permutations:", list(itertools.permutations("AB", 2)))

# --- 5. groupby (data must be sorted by key) ---
data = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot")]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
