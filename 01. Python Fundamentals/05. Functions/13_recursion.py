# 13 — Recursion (function calls itself)
# Run: python 13_recursion.py
#
# Every recursive function needs:
#   1. Base case (stop condition)
#   2. Recursive step (smaller subproblem)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("factorial(5) =", factorial(5))

# --- 1. Sum 1 to n ---
def sum_to(n):
    if n <= 0:
        return 0
    return n + sum_to(n - 1)

print("sum_to(5) =", sum_to(5))

# --- 2. Fibonacci (educational; slow for large n) ---
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print("fib(7) =", fib(7))

# --- 3. Recursion depth limit ---
# Python stops after ~1000 nested calls by default.
# Deep recursion -> use a loop instead.

def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(5)
