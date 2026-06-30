# 03 — Strings: creation, indexing, immutability
# Run: python 03_strings_basics.py

s1 = "Hello it's World"
s2 = 'This is "new" statement'
s3 = """hello this is new world
on multiple lines"""

print(s1)
print(s2)
print(s3)

# --- 1. Indexing ---
print("s1[0] =", s1[0])
print("s1[7] =", s1[7])
print("s1[-1] =", s1[-1])

# --- 2. Slicing ---
print("s1[6:10] =", s1[6:10])
print("s1[4:] =", s1[4:])
print("s1[:8] =", s1[:8])
print("s1[::-1] =", s1[::-1])

# --- 3. Immutable — cannot assign to a character ---
# s1[0] = "h"   # Uncomment -> TypeError

# --- 4. Iterate ---
for ch in s1:
    print(ch, end=" ")
print()

for i in range(len(s1)):
    print(s1[i], end="")
print()

# --- 5. Concatenation and repetition ---
print("Hi" + " " + "there")
print("ha" * 3)
