# 11 — else clause on for and while loops
# Run: python 11_for_while_else.py
#
# else runs when the loop finishes normally (no break).
# If break runs, else is skipped.

# --- 1. for-else ---
for i in range(3):
    print("for", i)
else:
    print("for completed without break")

# --- 2. for-else with break ---
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
else:
    print("not printed — break happened")
print()

# --- 3. while-else ---
count = 0
while count < 3:
    print("while", count)
    count += 1
else:
    print("while finished normally")

# --- 4. Practical: search with for-else ---
nums = [2, 4, 6, 8]
target = 5
for n in nums:
    if n == target:
        print("Found", target)
        break
else:
    print(target, "not in list")
