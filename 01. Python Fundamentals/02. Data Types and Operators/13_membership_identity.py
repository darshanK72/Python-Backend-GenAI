# 13 — Membership (in) and identity (is) operators
# Run: python 13_membership_identity.py

# --- 1. in / not in — test if value is inside a collection ---
s1 = "hello world, this is sparta"
s2 = "sparta"
print("s2 in s1:", s2 in s1)
print("s2 not in s1:", s2 not in s1)

nums = [10, 20, 30]
print("20 in nums:", 20 in nums)
print("99 not in nums:", 99 not in nums)

person = {"name": "Darshan", "city": "Nashik"}
print("'name' in person:", "name" in person)       # checks keys
print("'Darshan' in person:", "Darshan" in person)

# --- 2. is / is not — same object in memory? ---
p = 40
q = 40
print("p is q:", p is q)           # small ints may be cached; often True

list_a = [1, 2]
list_b = [1, 2]
print("list_a is list_b:", list_a is list_b)       # False — different lists
print("list_a == list_b:", list_a == list_b)       # True — same content

list_c = list_a
print("list_a is list_c:", list_a is list_c)       # True — alias

# --- 3. is None (always use is for None) ---
value = None
print("value is None:", value is None)
print("value is not None:", value is not None)

# --- 4. == compares values; is compares identity ---
x = 1000
y = 1000
print("x == y:", x == y)
print("x is y:", x is y)   # may be False — large ints are separate objects
