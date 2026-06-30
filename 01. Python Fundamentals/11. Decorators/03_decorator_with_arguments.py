# 03 — Decorators with arguments
# Run: python 03_decorator_with_arguments.py

from functools import wraps

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say(msg):
    print(msg)

say("Hello")

# --- 2. Optional validation decorator ---
def require_positive(func):
    @wraps(func)
    def wrapper(n):
        if n <= 0:
            raise ValueError("n must be positive")
        return func(n)
    return wrapper

@require_positive
def square_root_approx(n):
    return n ** 0.5

print("sqrt(16) =", square_root_approx(16))
