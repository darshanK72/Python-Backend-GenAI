# 05 — Ternary expression and match-case
# Run: python 05_ternary_and_match.py

# --- 1. Ternary (conditional expression) ---
# value_if_true if condition else value_if_false
a, b = 10, 25
greater = a if a > b else b
print("greater =", greater)

status = "pass" if 55 >= 40 else "fail"
print("status =", status)

# --- 2. match-case (Python 3.10+) — like switch in other languages ---
day = "Monday"

match day:
    case "Monday":
        print("Start of work week")
    case "Friday":
        print("Almost weekend")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Midweek day")   # _ = default (wildcard)

# --- 3. match with values (pattern matching intro) ---
command = "quit"

match command:
    case "start":
        print("Starting...")
    case "stop" | "quit":
        print("Stopping...")
    case _:
        print("Unknown command")
