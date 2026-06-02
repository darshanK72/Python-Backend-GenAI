# 07 — Naming rules, style, and constants
# Run: python 07_naming.py
#
# Good names make code easy to read. Python has strict rules and soft conventions.

# --- 1. Valid names ---
# Letters (a-z, A-Z), digits (0-9), underscore _ — but NOT starting with a digit.
user_name = "alex"
score2 = 100
_private = "leading underscore is allowed"

print("user_name =", user_name)
print("score2 =", score2)

# --- 2. Invalid names (uncomment ONE line at a time to see the error) ---
# 2score = 10           # SyntaxError — cannot start with a digit
# my-var = 5            # SyntaxError — hyphen is minus, not part of the name
# class = 1             # SyntaxError — class is a reserved keyword

# --- 3. Reserved keywords ---
# Words like if, else, for, while, def, class, return, import, True, False, None
# cannot be used as variable names.
# import keyword
# print(keyword.kwlist)   # Uncomment to print the full list

# --- 4. Case-sensitive ---
age = 20
Age = 30
print("age =", age, "| Age =", Age)       # two different variables

# --- 5. Constants (by convention) ---
# ALL_CAPS signals "do not change this value" — convention only, not enforced.
MAX_LOGIN_ATTEMPTS = 3
PI = 3.14159
print("MAX_LOGIN_ATTEMPTS =", MAX_LOGIN_ATTEMPTS, "| PI =", PI)

# --- 6. snake_case (standard for variables and functions) ---
total_marks = 450
student_count = 30
print("total_marks =", total_marks, "| student_count =", student_count)

# --- 7. Descriptive vs vague names ---
# Good: years_experience = 5
# Weak: x = 5
years_experience = 5
print("years_experience =", years_experience)

# --- 8. Reusing a name shadows the old value ---
value = 10
print("value =", value)
value = 20
print("value after reassignment =", value)
