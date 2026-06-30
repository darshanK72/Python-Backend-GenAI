# 02 — try / except
# Run: python 02_try_except.py
#
# try: code that might fail
# except ExceptionType: handle that error

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    return result

print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))

# --- 1. Catch and use the exception object ---
def parse_int(text):
    try:
        return int(text)
    except ValueError as e:
        print("Invalid integer:", e)
        return None

print("parse '42' =", parse_int("42"))
print("parse 'hi' =", parse_int("hi"))

# --- 2. Multiple types (same handler) ---
def process(value):
    try:
        return 100 / value
    except (ZeroDivisionError, TypeError) as e:
        print("Error:", type(e).__name__, e)
        return None

print(process(0))
print(process("ten"))
