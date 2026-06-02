# 14 — Abstract base classes (ABC)
# Run: python 14_abstract_classes.py
#
# ABC forces subclasses to implement certain methods.

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class UPIPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paid {amount} via UPI")

    def refund(self, amount):
        print(f"Refunded {amount} via UPI")

class CardPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paid {amount} via Card")

    def refund(self, amount):
        print(f"Refunded {amount} via Card")

# pg = PaymentGateway()   # Uncomment -> TypeError (cannot instantiate ABC)

upi = UPIPayment()
upi.pay(500)

# --- Shared concrete method on ABC ---
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print(f"Area is {self.area():.2f}")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

sq = Square(4)
sq.describe()
