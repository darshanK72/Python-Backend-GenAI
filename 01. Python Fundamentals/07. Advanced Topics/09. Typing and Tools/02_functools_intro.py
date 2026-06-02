# 02 — functools helpers
# Run: python 02_functools_intro.py

from functools import partial, lru_cache, reduce

# --- 1. partial — fix some arguments ---
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
print("square(5) =", square(5))
print("cube(5) =", cube(5))

# --- 2. lru_cache — memoization ---
@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print("fib(30) =", fib(30))
print("cache info:", fib.cache_info())

# --- 3. reduce ---
nums = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, nums)
print("product =", product)
