# 09 — while loop
# Run: python 09_while_loop.py
#
# while condition:
#     block
#
# Repeats WHILE condition is True. Make sure the condition eventually becomes False.

# --- 1. Count from 1 to 5 ---
i = 1
while i <= 5:
    print("i =", i)
    i += 1

# --- 2. Count age 10 to 15 (sample) ---
age = 10
while age <= 15:
    print("your age is:", age)
    age += 1

# --- 3. while False never runs ---
while False:
    print("This never prints")

# --- 4. User-input style (simulated with a counter) ---
# Real pattern: while True: ... break when done
attempts = 0
while attempts < 3:
    print("Attempt", attempts + 1)
    attempts += 1

# --- 5. Infinite loop danger ---
# while True:
#     print("runs forever — use break or change condition")
