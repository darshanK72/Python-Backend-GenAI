# 01 — Why test?
# Run: python 01_why_test.py
#
# Testing = running your code with known inputs and checking the output
# matches what you expect. It catches bugs early and lets you change code
# with confidence.

from sample_code import add, is_even

# --- 1. Manual "testing" — just printing and eyeballing (not reliable) ---
print("add(2, 3) =", add(2, 3))      # you have to read and judge yourself
print("is_even(4) =", is_even(4))

# Problem: nothing fails automatically if the answer is wrong.

# --- 2. A check that actually fails when wrong ---
result = add(2, 3)
if result != 5:
    print("BUG: add(2, 3) should be 5 but got", result)
else:
    print("OK: add(2, 3) == 5")

# --- 3. The same idea, shorter, with assert (next lesson) ---
assert add(2, 3) == 5
assert is_even(10) is True
print("All quick checks passed")

# Takeaway: good tests are automatic — they shout when something breaks,
# instead of relying on you to spot a wrong number in the output.
