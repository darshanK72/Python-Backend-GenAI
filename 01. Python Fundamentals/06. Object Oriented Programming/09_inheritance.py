# 09 — Inheritance (reuse and extend classes)
# Run: python 09_inheritance.py
#
# Child class inherits attributes and methods from parent (base class).

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# --- 1. Use parent and child ---
a = Animal("Generic")
d = Dog("Buddy")
c = Cat("Whiskers")

a.speak()
d.speak()
c.speak()

# --- 2. isinstance and issubclass ---
print("isinstance(d, Dog):", isinstance(d, Dog))
print("isinstance(d, Animal):", isinstance(d, Animal))
print("issubclass(Dog, Animal):", issubclass(Dog, Animal))

# --- 3. super() calls parent implementation ---
class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def speak(self):
        super().speak()
        print(f"{self.name} can fly: {self.can_fly}")

b = Bird("Tweety", True)
b.speak()
