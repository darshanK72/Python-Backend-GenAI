# 01 — Exceptions (introduction)
# Run: python 01_exceptions_intro.py
#
# An exception = error detected at runtime.
# Without handling, the program stops with a traceback.

# --- 1. Common built-in exceptions ---
# ZeroDivisionError, ValueError, TypeError, IndexError, KeyError, FileNotFoundError

print("10 / 2 =", 10 / 2)

# Uncomment one at a time to see the error type:
# print(10 / 0)           # ZeroDivisionError
# print(int("abc"))       # ValueError
# print([1, 2][99])       # IndexError
# print({"a": 1}["b"])    # KeyError

# --- 2. Reading tracebacks ---
# Bottom line = actual error type and message
# Lines above show which file and line caused it

def divide(a, b):
    return a / b

print("divide(10, 2) =", divide(10, 2))
