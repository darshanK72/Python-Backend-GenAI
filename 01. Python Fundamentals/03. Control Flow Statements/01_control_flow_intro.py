# 01 — Control flow (overview)
# Run: python 01_control_flow_intro.py
#
# Control flow = the order in which statements run.
# By default, Python runs top to bottom, one line at a time.
# You change that with: if / elif / else, for, while, break, continue.

# --- 1. Sequential (default) ---
print("Step 1")
print("Step 2")
print("Step 3")

# --- 2. Conditional — run a block only when a condition is True ---
score = 85
if score >= 40:
    print("Passed")

# --- 3. Loop — repeat a block ---
for i in range(3):
    print("loop", i)

# --- 4. Indentation matters ---
# The block under if/for/while MUST be indented (usually 4 spaces).
# Same indentation level = same block.

x = 10
if x > 5:
    print("x is big")
    print("still inside if")
print("back to main flow")
