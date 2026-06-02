# 05 — Keyword arguments when calling
# Run: python 05_keyword_arguments.py
#
# Pass name=value to match parameters by name (order then optional).

def display(a, b, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)

# --- 1. Keyword args — order does not matter ---
display(c=2, a=6, b=22)

# --- 2. Mix positional then keyword ---
display(1, c=3, b=2)

# display(a=1, 2, 3)   # Uncomment -> SyntaxError (positional after keyword)

# --- 3. Readable calls with many parameters ---
def create_user(name, age, city, active=True):
    print(name, age, city, active)

create_user("Darshan", age=25, city="Nashik")
create_user(name="Asha", city="Pune", age=22, active=False)

# --- 4. Unpacking a dict into keyword arguments ---
settings = {"a": 10, "b": 20, "c": 30}
display(**settings)
