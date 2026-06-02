# 07 — @classmethod and @staticmethod
# Run: python 07_class_and_static_methods.py

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def display(self):
        print(f"{self.year}-{self.month:02d}-{self.day:02d}")

    @classmethod
    def from_string(cls, date_str):
        # cls is the class (Date), not an instance
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)

    @staticmethod
    def is_leap_year(year):
        # no self or cls — just a function grouped in the class
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

d1 = Date(2026, 6, 2)
d1.display()

d2 = Date.from_string("2025-12-25")
d2.display()

print("2024 leap?", Date.is_leap_year(2024))

# --- Factory pattern example ---
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod
    def guest(cls):
        return cls("Guest", "guest")

    @classmethod
    def admin(cls, name):
        return cls(name, "admin")

u1 = User.guest()
u2 = User.admin("Darshan")
print(u1.name, u1.role)
print(u2.name, u2.role)
