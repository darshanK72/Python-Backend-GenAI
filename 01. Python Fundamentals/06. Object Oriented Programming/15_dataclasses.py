# 15 — dataclasses (less boilerplate for data-heavy classes)
# Run: python 15_dataclasses.py
#
# @dataclass auto-generates __init__, __repr__, and more.

from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    age: int
    marks: float

s1 = Student("Darshan", 25, 88.5)
s2 = Student("Meera", 22, 92.0)
print(s1)
print(s2)

# --- Default values ---
@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

p = Product("Notebook", 49.99)
print(p)

# --- field() for mutable defaults ---
@dataclass
class Team:
    name: str
    members: list = field(default_factory=list)

t = Team("Alpha")
t.members.append("Asha")
print(t)

# --- dataclass can still have methods ---
@dataclass
class Point:
    x: int
    y: int

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

pt = Point(3, 4)
print("distance =", pt.distance_from_origin())
