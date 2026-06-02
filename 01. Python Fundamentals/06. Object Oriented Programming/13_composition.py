# 13 — Composition ("has-a" vs "is-a")
# Run: python 13_composition.py
#
# Inheritance = is-a (Dog is an Animal)
# Composition = has-a (Car has an Engine)

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine {self.horsepower}hp started")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine   # composition

    def drive(self):
        self.engine.start()
        print(f"{self.brand} is driving")

car = Car("Toyota", Engine(150))
car.drive()

# --- Composition often beats deep inheritance ---
class Address:
    def __init__(self, city, pincode):
        self.city = city
        self.pincode = pincode

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def show(self):
        print(f"{self.name} lives in {self.address.city} ({self.address.pincode})")

cust = Customer("Darshan", Address("Nashik", "422001"))
cust.show()
