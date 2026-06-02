# 12 — Sets: unique, unordered collections
# Run: python 12_set_basics.py

# --- 1. Create sets (duplicates removed) ---
s1 = {4, 5, 6, 63, 23, 6, 2, 36, 7, 23, 5}
print("s1:", s1)

s2 = {"abcd", "hello", 56246, 63.34, True}
print("s2:", s2)

# --- 2. Empty set must use set(), not {} ---
empty = set()
print("empty set:", empty, type(empty))
# {} creates an empty dict

# --- 3. Create from list (remove duplicates) ---
l1 = [1, 265, 73, 3, 3, 3, 63, 63]
unique = set(l1)
print("unique from list:", unique)

# --- 4. Iterate (order not guaranteed) ---
for item in s1:
    print(item, end=" ")
print()

# --- 5. Membership (fast lookup) ---
print("5 in s1:", 5 in s1)

# --- 6. Add and update ---
s2.add(67)
s2.add(67)
print("after add:", s2)

s1.update([100, 200, 5])
print("after update:", s1)

# --- 7. Remove ---
to_remove = next(iter(s1))   # pick any existing element
s1.remove(to_remove)         # KeyError if element not in set
print("after remove(", to_remove, "):", s1, sep="")

s1.discard(999)              # no error if missing
print("after discard(999):", s1)
print("pop():", s1.pop())
