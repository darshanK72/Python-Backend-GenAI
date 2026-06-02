# 03 — Instance methods and self
# Run: python 03_instance_methods.py
#
# Methods are functions inside a class.
# self is the current instance (passed automatically).

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def describe(self):
        print(f"Rectangle {self.width}x{self.height}, area={self.area()}")

r = Rectangle(5, 3)
print("area =", r.area())
print("perimeter =", r.perimeter())
r.describe()

# --- 1. Calling methods ---
# r.area() is shorthand for Rectangle.area(r)

print("explicit call:", Rectangle.area(r))

# --- 2. Method can use other methods on same object ---
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self, step=1):
        self.value += step

    def reset(self):
        self.value = 0

    def show(self):
        print("count =", self.value)

c = Counter()
c.increment()
c.increment(5)
c.show()
c.reset()
c.show()
