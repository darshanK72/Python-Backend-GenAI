# 01 — Threading basics
# Run: python 01_threading_basics.py
#
# Threads share memory; good for I/O-bound tasks (network, files).
# CPU-heavy work often needs multiprocessing (not covered deeply here).

from threading import Thread
from time import sleep

def say_hello():
    for _ in range(3):
        print("HELLO")
        sleep(0.3)

def say_hi():
    for _ in range(3):
        print("HI")
        sleep(0.3)

# --- 1. Subclassing Thread ---
class HelloThread(Thread):
    def run(self):
        say_hello()

t1 = HelloThread()
t2 = Thread(target=say_hi)

t1.start()
sleep(0.1)
t2.start()

t1.join()
t2.join()
print("Both threads finished")
