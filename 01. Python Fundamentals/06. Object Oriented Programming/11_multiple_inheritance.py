# 11 — Multiple inheritance and MRO
# Run: python 11_multiple_inheritance.py
#
# A class can inherit from more than one parent.
# MRO = Method Resolution Order (which class is searched first).

class Flyer:
    def move(self):
        print("Flying")

class Swimmer:
    def move(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    def move(self):
        print("Duck moves on land, then:")
        super().move()   # follows MRO: Flyer.move next

d = Duck()
d.move()

print("MRO:", [c.__name__ for c in Duck.__mro__])

# --- Mixing capabilities ---
class Logger:
    def log(self, msg):
        print("[LOG]", msg)

class Worker:
    def work(self):
        print("Working...")

class Developer(Logger, Worker):
    def run_task(self):
        self.log("Task started")
        self.work()
        self.log("Task done")

dev = Developer()
dev.run_task()

# Keep inheritance shallow and clear — favor composition when possible.
