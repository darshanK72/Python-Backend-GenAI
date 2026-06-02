# 05 — Practical comprehension patterns
# Run: python 05_comprehension_patterns.py

words = ["hello", "world", "python", "code"]

# --- 1. Lengths ---
lengths = [len(w) for w in words]
print("lengths:", lengths)

# --- 2. Strip and lower a list of lines ---
lines = ["  Hello ", "  WORLD ", "  Python  "]
clean = [line.strip().lower() for line in lines]
print("clean:", clean)

# --- 3. Index with enumerate in a comp ---
indexed = [f"{i}: {w}" for i, w in enumerate(words)]
print("indexed:", indexed)

# --- 4. Zip into dict ---
keys = ["name", "age", "city"]
values = ["Darshan", 25, "Nashik"]
person = {k: v for k, v in zip(keys, values)}
print("person:", person)

# --- 5. When NOT to use comprehension ---
# If logic is long or has many branches, use a normal for-loop for clarity.
