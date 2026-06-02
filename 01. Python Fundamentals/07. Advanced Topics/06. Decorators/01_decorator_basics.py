# 01 — Decorator basics
# Run: python 01_decorator_basics.py
#
# A decorator wraps a function to add behavior before/after it runs.

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

print("result =", add(3, 4))

# --- Same as: add = log_calls(add) ---

# --- 2. Timing decorator ---
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f}s")
        return result
    return wrapper

@timer
def slow():
    total = sum(range(100000))
    return total

slow()
