# 01 — Functions (introduction)
# Run: python 01_functions_intro.py
#
# A function is a reusable block of code with a name.
# Benefits: less repetition, easier to read, easier to test.

# --- 1. Define and call ---
def greet():
    print("Hello from a function!")

greet()
greet()   # call as many times as you like

# --- 2. Why use functions? ---
# Without a function you repeat code:
print("---")
print("Task A: setup")
print("Task A: run")
print("---")
print("Task B: setup")
print("Task B: run")

# With a function you write once:
def run_task(name):
    print("---")
    print(f"Task {name}: setup")
    print(f"Task {name}: run")

run_task("A")
run_task("B")

# --- 3. Syntax reminder ---
# def function_name(parameters):
#     indented body
#     return value   # optional
