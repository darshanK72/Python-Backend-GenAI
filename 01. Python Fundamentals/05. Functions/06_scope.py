# 06 — Variable scope (local vs global)
# Run: python 06_scope.py
#
# Local = inside a function. Global = module level.

count = 100   # global

def increment():
    local_count = 1   # local — different from global count
    local_count += 1
    print("inside increment, local_count =", local_count)

increment()
print("outside, global count =", count)

# --- 1. Reading global inside function works ---
message = "Hello"

def show_message():
    print(message)   # reads global

show_message()

# --- 2. Assigning creates a local variable ---
def broken():
    # print(message)   # UnboundLocalError if you assign below without global
    message = "Hi"     # local shadows global

broken()
print("global message still:", message)

# --- 3. global keyword (use sparingly) ---
total = 0

def add_to_total(n):
    global total
    total += n

add_to_total(5)
add_to_total(10)
print("total =", total)

# --- 4. Prefer returning values instead of global ---
def add_values(a, b):
    return a + b

print("sum =", add_values(3, 4))
