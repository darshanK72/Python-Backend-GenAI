# 06 — @property (controlled attribute access)
# Run: python 06_properties.py
#
# property lets you use methods like attributes: obj.radius instead of obj.get_radius()

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(5)
print("radius =", c.radius)
print("area =", c.area)
c.radius = 10
print("new area =", c.area)

# c.radius = -1   # Uncomment -> ValueError

# --- Read-only property (no setter) ---
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

p = Person("Darshan", "Khairnar")
print(p.full_name)
