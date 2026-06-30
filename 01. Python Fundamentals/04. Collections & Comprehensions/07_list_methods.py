# 07 — List methods
# Run: python 07_list_methods.py

l1 = [5, 252, 23, 73, 4, 36, 6, 35, 36, 3, 563]
print("start:", l1)

# --- 1. Add items ---
l1.append(700)              # one item at end
print("append(700):", l1)

l2 = [76, 703, 23]
l1.extend(l2)               # add all items from another iterable
print("extend(l2):", l1)

l1.insert(2, "Banana")        # insert at index
print("insert(2, 'Banana'):", l1)

# --- 2. Remove items ---
print("pop() =", l1.pop())    # remove and return last
print("after pop:", l1)

l1.remove("Banana")           # remove first matching value
print("remove('Banana'):", l1)

# --- 3. Search and count ---
print("index(35) =", l1.index(35))
print("count(36) =", l1.count(36))

# --- 4. Sort and reverse ---
l1.sort()                     # in-place ascending
print("sort():", l1)
l1.reverse()
print("reverse():", l1)

# --- 5. copy and clear ---
l3 = l1.copy()                # shallow copy
print("copy:", l3)
l2.clear()
print("l2 after clear:", l2)

# --- 6. Other useful methods ---
nums = [3, 1, 4, 1, 5]
print("min:", min(nums), "max:", max(nums), "sum:", sum(nums))
