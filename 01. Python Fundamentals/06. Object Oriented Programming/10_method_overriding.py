# 10 — Method overriding and polymorphism
# Run: python 10_method_overriding.py
#
# Overriding = child provides its own version of a parent method.
# Polymorphism = same interface, different behavior per type.

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

# --- Polymorphism: one function, many types ---
def print_area(shape):
    print(f"{shape.__class__.__name__} area =", shape.area())

shapes = [Rectangle(4, 5), Circle(3)]
for s in shapes:
    print_area(s)

# --- isinstance check (when needed) ---
def describe(obj):
    if isinstance(obj, Rectangle):
        print("Rectangle", obj.width, "x", obj.height)
    elif isinstance(obj, Circle):
        print("Circle radius", obj.radius)

describe(shapes[0])
