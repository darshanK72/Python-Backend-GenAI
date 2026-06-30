# 04 — else and finally
# Run: python 04_else_finally.py
#
# else: runs only if try did NOT raise an exception
# finally: always runs (cleanup)

def read_number(text):
    try:
        n = int(text)
    except ValueError:
        print("Not a valid number")
        return None
    else:
        print("Converted successfully")
        return n
    finally:
        print("--- attempt finished ---")

print("result =", read_number("42"))
print()
print("result =", read_number("abc"))

# --- 1. finally for cleanup (even after return) ---
def demo_finally():
    try:
        print("in try")
        return "from try"
    finally:
        print("in finally (runs before return)")

print("demo_finally returned:", demo_finally())

# --- 2. Real use: close resources in finally (better: use with) ---
# file = open(...)
# try:
#     ...
# finally:
#     file.close()
