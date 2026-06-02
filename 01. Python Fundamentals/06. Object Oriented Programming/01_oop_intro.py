# 01 — Object-Oriented Programming (introduction)
# Run: python 01_oop_intro.py
#
# OOP organizes code around "objects" that combine:
#   - data (attributes / state)
#   - behavior (methods / functions on the object)
#
# Main ideas: encapsulation, inheritance, polymorphism, abstraction.

# --- 1. Procedural style (functions + separate data) ---
student_name = "Darshan"
student_marks = 88

def show_student(name, marks):
    print(f"{name}: {marks}")

show_student(student_name, student_marks)

# --- 2. OOP style (data + behavior bundled in a class) ---
class Student:
    def show(self):
        print(f"{self.name}: {self.marks}")

s = Student()
s.name = "Darshan"
s.marks = 88
s.show()

# --- 3. Why OOP helps ---
# - Models real-world things (User, Order, BankAccount)
# - Reuse through inheritance
# - Keeps related code together

print("\nKey terms:")
print("class  = blueprint")
print("object = instance built from a class")
