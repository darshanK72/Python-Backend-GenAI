# 04 — Default parameter values
# Run: python 04_default_parameters.py
#
# Defaults are used when the caller omits that argument.
# Defaults are evaluated once at function definition time (watch mutable defaults).

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Darshan")
greet("Darshan", "Hi")

# --- 1. Default must come after non-default parameters ---
def power(base, exponent=2):
    return base ** exponent

print("power(5) =", power(5))
print("power(5, 3) =", power(5, 3))

# --- 2. Common pattern: optional prefix/suffix ---
def make_url(path, domain="example.com", secure=True):
    scheme = "https" if secure else "http"
    return f"{scheme}://{domain}/{path}"

print(make_url("docs"))
print(make_url("api", domain="myapp.io", secure=False))

# --- 3. Mutable default pitfall (avoid this) ---
def bad_append(item, target=[]):   # same list reused every call!
    target.append(item)
    return target

print("bad:", bad_append(1))
print("bad again:", bad_append(2))   # [1, 2] — surprising!

def good_append(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target

print("good:", good_append(1))
print("good again:", good_append(2))   # [2] — correct
