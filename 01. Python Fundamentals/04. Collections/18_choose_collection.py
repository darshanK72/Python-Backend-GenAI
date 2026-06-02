# 18 — Which collection to use?
# Run: python 18_choose_collection.py
#
# Cheat sheet for picking the right structure.

print("Use str     -> text, immutable, indexed")
print("Use list    -> ordered items you will change or grow")
print("Use tuple   -> fixed records, return multiple values, dict keys")
print("Use set     -> unique items, membership tests, set math")
print("Use dict    -> lookup by key (name, id, label)")
print("Use range   -> number sequences in loops without storing a list")

# --- Quick demos ---
# Unique visitors from a log
visits = ["u1", "u2", "u1", "u3", "u2"]
print("unique users:", set(visits))

# Student lookup by roll number
roster = {101: "Asha", 102: "Ravi", 103: "Meera"}
print("roll 102:", roster[102])

# Coordinates that should not change
origin = (0, 0)

# Shopping cart (order matters, items change)
cart = ["book", "pen"]
cart.append("notebook")
print("cart:", cart)
