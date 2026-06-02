# 12 — Special (dunder) methods
# Run: python 12_special_methods.py
#
# Double-underscore methods hook into Python syntax and built-ins.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError("index out of range")

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print("v1 + v2 =", v3)
print("v1 == v2:", v1 == v2)
print("len(v1) =", len(v1))
print("v1[0] =", v1[0])

# --- __bool__ for truthiness ---
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def __bool__(self):
        return len(self.items) > 0

q = Queue()
if not q:
    print("queue empty")
q.push(10)
if q:
    print("queue has items")
