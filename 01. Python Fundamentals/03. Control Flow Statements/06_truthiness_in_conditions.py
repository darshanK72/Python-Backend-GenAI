# 06 — Truthiness in if conditions
# Run: python 06_truthiness_in_conditions.py
#
# if does not need "== True". It runs the block when the value is "truthy".

# --- 1. Falsy values: False, 0, 0.0, "", None, [], (), {}, set() ---
name = "Darshan"
if name:
    print("Name is set:", name)

empty = ""
if not empty:
    print("String is empty")

items = []
if items:
    print("List has items")
else:
    print("List is empty")

# --- 2. Explicit comparison when needed ---
count = 0
if count == 0:          # clearer when you mean exactly zero
    print("count is zero")

# --- 3. Combining with and / or ---
username = "admin"
password = "secret"
if username and password:
    print("Both fields provided")

# --- 4. Membership in conditions ---
email = "user@example.com"
if "@" in email:
    print("Looks like an email")
