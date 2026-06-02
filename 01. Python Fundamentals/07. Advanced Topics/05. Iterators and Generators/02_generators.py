# 02 — Generator functions (yield)
# Run: python 02_generators.py
#
# yield pauses the function and returns a value; resumes on next().

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(5):
    print(x, end=" ")
print()

# --- 1. Generator object ---
gen = countdown(3)
print(next(gen))
print(next(gen))
print(list(gen))

# --- 2. Infinite generator (use with care) ---
def naturals(start=1):
    n = start
    while True:
        yield n
        n += 1

nums = naturals()
print([next(nums) for _ in range(5)])

# --- 3. Fibonacci generator ---
def fib(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

print(list(fib(10)))
