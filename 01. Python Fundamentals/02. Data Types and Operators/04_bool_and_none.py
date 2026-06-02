# 04 — bool and None
# Run: python 04_bool_and_none.py

# --- 1. bool literals ---
is_active = True
is_empty = False
print("True, False:", is_active, is_empty)

# --- 2. bool() converts other types ---
print("bool(0) =", bool(0))
print("bool(42) =", bool(42))
print('bool("") =', bool(""))
print('bool("hi") =', bool("hi"))
print("bool([]) =", bool([]))
print("bool([1]) =", bool([1]))

# --- 3. Falsy values (evaluate to False in conditions) ---
# 0, 0.0, "", None, [], (), {}, set()
print("Falsy check None:", bool(None))

# --- 4. None ---
# None = "no value". Only one instance; compare with "is", not ==
data = None
print("data is None:", data is None)

missing = None
found = None
print("missing is found:", missing is found)   # True — same singleton object

# --- 5. bool in arithmetic (treated as 1 and 0) ---
print("True + True =", True + True)
print("False + 5 =", False + 5)
