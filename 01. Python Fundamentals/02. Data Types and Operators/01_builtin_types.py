# 01 — Built-in data types (overview)
# Run: python 01_builtin_types.py
#
# Every value in Python has a type. type(value) tells you which one.
# Types are grouped below; collections are covered in depth in folder 05.

# --- 1. Numeric types ---
age = 21
marks = 88.6
voltage = 3 + 4j
print("int:", age, type(age))
print("float:", marks, type(marks))
print("complex:", voltage, type(voltage))

# --- 2. Text ---
name = "Darshan"
print("str:", name, type(name))

# --- 3. Boolean ---
is_student = True
print("bool:", is_student, type(is_student))

# --- 4. None (absence of value) ---
middle_name = None
print("NoneType:", middle_name, type(middle_name))

# --- 5. Sequence types (ordered; details in folder 05) ---
numbers = [10, 20, 30]           # list — mutable
coordinates = (10.5, 20.1)       # tuple — immutable
print("list:", numbers, type(numbers))
print("tuple:", coordinates, type(coordinates))

# --- 6. Set (unordered, unique items) ---
unique_ids = {1, 2, 3, 2}
print("set:", unique_ids, type(unique_ids))

# --- 7. Dictionary (key -> value mapping) ---
student = {"roll_no": 21, "name": "Darshan"}
print("dict:", student, type(student))

# --- 8. Mutable vs immutable (important idea) ---
# Immutable: int, float, str, tuple, bool, None — cannot change "in place"
# Mutable: list, dict, set — can add/remove/change items
x = 10
x = 20          # rebinding the name, not changing the int 10 itself
print("Reassigned int x =", x)
