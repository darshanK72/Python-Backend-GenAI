# 14 — Combining input() with control flow (interactive)
# Run: python 14_input_and_control_flow.py
#
# This file uses input() — run it yourself and type answers.

# --- 1. Compare two numbers ---
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First is greater")
elif a < b:
    print("Second is greater")
else:
    print("Both are equal")

# --- 2. Greatest of three ---
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x > y and x > z:
    print("Largest:", x)
elif y > x and y > z:
    print("Largest:", y)
else:
    print("Largest:", z)

# --- 3. Simple menu with while ---
# Uncomment to try:
# while True:
#     print("\n1. Greet  2. Quit")
#     choice = input("Choice: ")
#     if choice == "1":
#         name = input("Name: ")
#         print("Hello,", name)
#     elif choice == "2":
#         print("Bye")
#         break
#     else:
#         print("Invalid option")
