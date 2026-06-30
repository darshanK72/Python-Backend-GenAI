# 04 — Nested if (if inside if)
# Run: python 04_nested_if.py

age = 22
has_ticket = True

if age >= 18:
    print("Age OK")
    if has_ticket:
        print("Entry allowed")
    else:
        print("Need a ticket")
else:
    print("Too young")

# --- Leap year (classic nested logic) ---
year = 2000

if year % 100 == 0:
    if year % 400 == 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
else:
    if year % 4 == 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

# --- Flattened version (same logic, often easier to read) ---
year = 2016
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(year, "leap?" , is_leap)
