# 16 — Practical OOP examples
# Run: python 16_practical_examples.py

# --- 1. Student with grades ---
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.grades = []

    def add_grade(self, subject, score):
        self.grades.append({"subject": subject, "score": score})

    def average(self):
        if not self.grades:
            return 0
        return sum(g["score"] for g in self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} (#{self.roll_no}) avg={self.average():.1f}"

s = Student("Darshan", 101)
s.add_grade("Math", 90)
s.add_grade("Science", 85)
print(s)

# --- 2. Shopping cart ---
class CartItem:
    def __init__(self, name, price, qty=1):
        self.name = name
        self.price = price
        self.qty = qty

    def total(self):
        return self.price * self.qty

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(i.total() for i in self.items)

cart = ShoppingCart()
cart.add(CartItem("Book", 299, 2))
cart.add(CartItem("Pen", 20, 5))
print("cart total =", cart.total())

# --- 3. Library book borrow ---
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(self.title, "already borrowed")
            return False
        self.is_borrowed = True
        print("Borrowed:", self.title)
        return True

    def return_book(self):
        self.is_borrowed = False
        print("Returned:", self.title)

book = Book("Clean Code", "978-0132350884")
book.borrow()
book.borrow()
book.return_book()
