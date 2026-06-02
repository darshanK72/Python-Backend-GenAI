# 03 — return statement
# Run: python 03_return_values.py
#
# return sends a value back to the caller and exits the function.

def square(n):
    return n * n

print("square(5) =", square(5))

# --- 1. Store result in a variable ---
area = square(10)
print("area =", area)

# --- 2. Use return value in expressions ---
print("square(3) + square(4) =", square(3) + square(4))

# --- 3. Early return ---
def absolute(x):
    if x < 0:
        return -x
    return x

print("absolute(-7) =", absolute(-7))

# --- 4. Return multiple values (as a tuple) ---
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([3, 9, 1, 7])
print("min =", low, "max =", high)

# --- 5. factorial example ---
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

print("factorial(5) =", factorial(5))

# --- 6. No return -> None ---
def noop():
    pass

print("noop() =", noop())
