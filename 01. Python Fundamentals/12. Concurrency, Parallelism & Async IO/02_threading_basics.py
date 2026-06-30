# 02 — Threading basics
# Run: python 02_threading_basics.py
#
# Threads run inside one process and SHARE memory.
# Great for I/O-bound tasks (network, files) where threads spend time waiting.
# start() launches the thread; join() waits for it to finish.

from threading import Thread, current_thread
from time import sleep

def say(word):
    for _ in range(3):
        # current_thread().name helps you see which thread is printing.
        print(f"[{current_thread().name}] {word}")
        sleep(0.3)

# --- 1. Run a function in a thread (target=) ---
t1 = Thread(target=say, args=("HELLO",), name="hello-thread")
t2 = Thread(target=say, args=("HI",), name="hi-thread")

t1.start()
sleep(0.1)   # stagger so the output interleaves visibly
t2.start()

t1.join()
t2.join()
print("Both target threads finished")
print("-" * 30)

# --- 2. Subclassing Thread (override run) ---
# Useful when a thread needs its own state or setup.
class CounterThread(Thread):
    def __init__(self, limit):
        super().__init__()
        self.limit = limit
        self.total = 0   # store a result on the instance

    def run(self):
        for i in range(1, self.limit + 1):
            self.total += i

worker = CounterThread(limit=5)
worker.start()
worker.join()
print("CounterThread total:", worker.total)

# --- 3. is_alive() tells you if a thread is still running ---
slow = Thread(target=sleep, args=(0.5,))
slow.start()
print("alive right after start?", slow.is_alive())
slow.join()
print("alive after join?", slow.is_alive())
