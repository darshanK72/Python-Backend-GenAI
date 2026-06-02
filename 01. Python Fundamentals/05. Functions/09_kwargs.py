# 09 — **kwargs (variable keyword arguments)
# Run: python 09_kwargs.py
#
# **kwargs collects extra keyword arguments into a dictionary.

def show(**data):
    for key, value in data.items():
        print(f"{key} = {value}")

show(c=2, a=6, b=22)

# --- 1. Mix regular params with **kwargs ---
def build_profile(name, **extra):
    profile = {"name": name}
    profile.update(extra)
    return profile

print(build_profile("Darshan", city="Nashik", age=25))

# --- 2. Unpack dict into keyword arguments ---
options = {"a": 1, "b": 2, "c": 3}

def display(a, b, c):
    print(a, b, c)

display(**options)

# --- 3. **kwargs is a dict ---
def debug(**kwargs):
    print(type(kwargs), kwargs)

debug(x=10, y=20)
