# 08 — range() with for loops
# Run: python 08_range_and_for.py
#
# range(stop)           -> 0, 1, ..., stop-1
# range(start, stop)    -> start, ..., stop-1
# range(start, stop, step)

# --- 1. range(10) — 0 to 9 ---
print("range(10):", list(range(10)))

# --- 2. range(5, 15) — 5 to 14 ---
print("range(5, 15):", list(range(5, 15)))

# --- 3. range(2, 20, 2) — even numbers from 2 to 18 ---
print("range(2, 20, 2):", list(range(2, 20, 2)))

# --- 4. Print 1 to 10 ---
for i in range(1, 11):
    print(i, end=" ")
print()

# --- 5. Print even numbers 2 to 100 ---
for i in range(2, 101, 2):
    print(i, end=" ")
print()

# --- 6. Countdown ---
for i in range(5, 0, -1):
    print(i, end=" ")
print("Go!")

# --- 7. Odd numbers 1 to 99 ---
for var in range(1, 100, 2):
    if var % 2 != 0:
        print(var, end=" ")
print()

# range() does not store all numbers in memory at once (efficient for large ranges)
