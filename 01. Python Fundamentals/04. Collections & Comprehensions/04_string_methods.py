# 04 — String methods
# Run: python 04_string_methods.py

s1 = "hello world this Is FIRST string"
print("original:", s1)

# --- 1. Case ---
print("capitalize:", s1.capitalize())
print("upper:", s1.upper())
print("lower:", s1.lower())
print("title:", s1.title())
print("swapcase:", s1.swapcase())

# --- 2. Tests (return True/False) ---
print("'abc'.isalpha():", "abc".isalpha())
print("'123'.isdigit():", "123".isdigit())
print("'abc123'.isalnum():", "abc123".isalnum())
print("'  '.isspace():", "  ".isspace())

# --- 3. Search ---
text = "hello this is sparta, welcome to world"
print("find('sparta'):", text.find("sparta"))       # -1 if missing
print("find('xyz'):", text.find("xyz"))
print("count('is'):", text.count("is"))
# print("index('xyz'):", text.index("xyz"))        # Uncomment -> ValueError

# --- 4. Strip whitespace or custom chars ---
s6 = "          hello         "
print("strip:", repr(s6.strip()))
print("lstrip:", repr(s6.lstrip()))
print("rstrip:", repr(s6.rstrip()))

s7 = "$$$hello$$$"
print("strip('$'):", s7.strip("$"))

# --- 5. split and join ---
print("split():", text.split())
print("split('-'):", "a-b-c".split("-"))
words = ["hello", "world", "python"]
print("join:", "-".join(words))

# --- 6. replace ---
print("replace:", text.replace("world", "Python"))

# --- 7. startswith / endswith ---
print("startswith('hello'):", text.startswith("hello"))
