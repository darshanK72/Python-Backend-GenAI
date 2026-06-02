# 02 — Comments
# Run: python 02_comments.py
#
# Comments are notes for humans. Python ignores them when running code.
# Use them to explain WHY something is done, not to repeat obvious code.

# --- 1. Single-line comment ---
# Everything after # on this line is a comment.
print("This line runs")

# --- 2. Inline comment (end of a line) ---
print("Result:", 10 + 5)  # addition happens first, then print

# --- 3. Comment out code temporarily ---
# print("This will NOT run because the whole line is commented")
print("This WILL run")

# --- 4. Multi-line block with triple quotes ---
# A string in """ ... """ can sit alone (not assigned to a variable).
# It does not print by itself — unlike a comment, Python still creates the string.
"""
This block is a string literal, often used at the top of a file
to describe what the program does.
Later you will use the same style as a docstring under functions.
"""
print("Triple-quoted text above was stored but not printed.")

# --- 5. When to comment ---
# Good:  tax = price * 0.18   # 18% GST
# Avoid: x = x + 1           # add 1 to x  (too obvious)
