# 02 — functools.wraps (preserve function metadata)
# Run: python 02_preserve_metadata.py

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper docstring"""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greet a person."""
    return f"Hello, {name}"

print("name:", greet.__name__)
print("doc:", greet.__doc__)
print(greet("Darshan"))

# Without @wraps, __name__ would be 'wrapper' and __doc__ would be lost.
