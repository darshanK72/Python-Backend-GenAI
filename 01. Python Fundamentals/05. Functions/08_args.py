# 08 — *args (variable positional arguments)
# Run: python 08_args.py
#
# *args collects extra positional arguments into a tuple.

def add_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print("add_all(1, 2) =", add_all(1, 2))
print("add_all(5, 62, 45) =", add_all(5, 62, 45))
print("add_all() =", add_all())

# --- 1. Mix normal parameters with *args ---
def intro(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}")

intro("Hello", "Asha", "Ravi", "Meera")

# --- 2. Unpack a list/tuple into positional args ---
nums = [10, 20, 30]
print("add_all(*nums) =", add_all(*nums))

# --- 3. *args name is convention — you can use another name ---
def show(*items):
    print(type(items), items)

show(1, 2, 3)
