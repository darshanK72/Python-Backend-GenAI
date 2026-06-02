# 07 — type(), isinstance(), and type hints (intro)
# Run: python 07_type_checking.py

value = 42

# --- 1. type() returns the class of an object ---
print("type(42) =", type(value))
print("type(42) is int:", type(value) is int)

# --- 2. isinstance() — preferred for checks (handles inheritance) ---
print("isinstance(42, int) =", isinstance(value, int))
print("isinstance(42, (int, float)) =", isinstance(value, (int, float)))

# --- 3. Converting types (see also folder 01, 05_typecasting) ---
s = str(100)
n = int("100")
print(s, n, type(s), type(n))

# --- 4. Type hints (documentation; not enforced at runtime by default) ---
def greet(name: str) -> str:
    return "Hello, " + name

message = greet("Darshan")
print(message)

# --- 5. id() — identity (memory address; CPython implementation detail) ---
a = [1, 2]
b = [1, 2]
c = a
print("a is c:", a is c)       # True — same object
print("a is b:", a is b)       # False — equal content, different objects
print("a == b:", a == b)       # True — same values
