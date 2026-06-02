# 04 — Instance attributes vs class attributes
# Run: python 04_instance_vs_class_attributes.py
#
# Instance attribute: unique per object (self.name)
# Class attribute: shared by all instances (defined on class)

class Employee:
    company = "Acme Corp"          # class attribute (shared)

    def __init__(self, name, salary):
        self.name = name           # instance attribute
        self.salary = salary

e1 = Employee("Asha", 50000)
e2 = Employee("Ravi", 60000)

print(e1.name, e1.company)
print(e2.name, e2.company)

# --- 1. Change class attribute for all (if not shadowed) ---
Employee.company = "New Acme"
print("e1.company =", e1.company)

# --- 2. Shadowing: instance attribute hides class attribute ---
e1.company = "Freelance"
print("e1.company =", e1.company)
print("e2.company =", e2.company)

# --- 3. Class attribute as default ---
class BankAccount:
    interest_rate = 0.04

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

a = BankAccount("Darshan", 1000)
b = BankAccount("Meera", 500)
print(a.owner, a.balance, a.interest_rate)
print(b.interest_rate)
