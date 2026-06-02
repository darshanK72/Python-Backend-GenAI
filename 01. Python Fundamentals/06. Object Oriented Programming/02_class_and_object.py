# 02 — class, object, and __init__
# Run: python 02_class_and_object.py
#
# class Name: defines a new type.
# object = Name() creates an instance.
# __init__ runs automatically after the object is created.

class Dog:
    def __init__(self, name, breed):
        self.name = name      # instance attribute
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

# --- 1. Create objects ---
d1 = Dog("Buddy", "Labrador")
d2 = Dog("Max", "Beagle")

print(d1.name, d1.breed)
d1.bark()
d2.bark()

# --- 2. Each object has its own data ---
d1.name = "Buddy Jr."
print("d1.name =", d1.name)
print("d2.name =", d2.name)

# --- 3. type and isinstance ---
print("type(d1) =", type(d1))
print("isinstance(d1, Dog) =", isinstance(d1, Dog))
