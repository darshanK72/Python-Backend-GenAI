# 03 — Multiple except blocks
# Run: python 03_multiple_except.py
#
# Put more specific exceptions before general ones.

def calculate(a, b, op):
    try:
        if op == "div":
            return a / b
        if op == "idx":
            items = [1, 2, 3]
            return items[b]
        return a + b
    except ZeroDivisionError:
        print("ZeroDivisionError: b cannot be 0 for division")
    except IndexError:
        print("IndexError: index out of range")
    except TypeError:
        print("TypeError: wrong types for operation")
    except Exception as e:
        print("Other error:", type(e).__name__, e)
    return None

print(calculate(10, 2, "add"))
print(calculate(10, 0, "div"))
print(calculate(10, 99, "idx"))

# --- Avoid bare except (bad practice) ---
# except:   # catches everything including KeyboardInterrupt
# Use except Exception: when you need a catch-all.
