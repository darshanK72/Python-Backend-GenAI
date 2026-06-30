# 08 — List copying (shallow vs reference)
# Run: python 08_list_copy_and_pitfalls.py

original = [1, 2, [10, 20]]

# --- 1. Assignment = same list (alias) ---
alias = original
alias.append(99)
print("original after alias.append:", original)

# --- 2. Shallow copy ---
original = [1, 2, [10, 20]]
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

copy1.append(3)
print("original:", original)
print("copy1:", copy1)

# --- 3. Shallow copy still shares nested objects ---
copy1[2].append(30)
print("original nested after copy1[2].append(30):", original)

# --- 4. Deep copy (when you need full independence) ---
import copy
original = [1, 2, [10, 20]]
deep = copy.deepcopy(original)
deep[2].append(99)
print("original:", original)
print("deep:", deep)
