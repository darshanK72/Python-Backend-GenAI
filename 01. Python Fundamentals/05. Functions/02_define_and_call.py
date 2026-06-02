# 02 — Define functions with parameters
# Run: python 02_define_and_call.py
#
# Parameters = names in the function definition.
# Arguments = actual values you pass when calling.

def add(a, b):
    return a + b

print("add(20, 50) =", add(20, 50))

# --- 1. Multiple parameters ---
def full_name(first, last):
    return first + " " + last

print(full_name("Darshan", "Khairnar"))

# --- 2. Positional arguments (order matters) ---
def describe(pet, age):
    print(f"{pet} is {age} years old")

describe("cat", 3)
# describe(3, "cat")   # still runs but meaning is wrong

# --- 3. Function with no return returns None ---
def say_hi(name):
    print("Hi,", name)

result = say_hi("Alex")
print("return value:", result)
