# 12 — Functions as values (first-class functions)
# Run: python 12_first_class_functions.py
#
# Functions are objects — you can assign, store in lists, and pass them around.

def greet(name):
    return f"Hello, {name}"

# --- 1. Assign to a variable ---
say = greet
print(say("Darshan"))

# --- 2. Pass function as argument ---
def apply_twice(func, value):
    return func(func(value))

def double(x):
    return x * 2

print("apply_twice(double, 3) =", apply_twice(double, 3))

# --- 3. Return a function from a function ---
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times3 = make_multiplier(3)
print("times3(7) =", times3(7))

# --- 4. List of functions ---
operations = [abs, round, str]
for op in operations:
    print(op(-3.7))
