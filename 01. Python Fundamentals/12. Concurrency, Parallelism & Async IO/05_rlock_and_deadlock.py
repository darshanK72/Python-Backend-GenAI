# 05 — RLock and deadlocks
# Run: python 05_rlock_and_deadlock.py
#
# RLock (reentrant lock) can be acquired multiple times by the SAME thread.
# A plain Lock would deadlock if one method holding the lock calls another
# method that also wants it. We also show how a deadlock happens and how
# consistent lock ordering avoids it.

from threading import Thread, Lock, RLock
import time

# --- 1. Why RLock: nested acquisition in the same thread ---
class Account:
    def __init__(self, balance):
        self.balance = balance
        self.lock = RLock()   # try Lock() here and deposit() would hang

    def deposit(self, amount):
        with self.lock:
            self.balance += amount

    def deposit_twice(self, amount):
        with self.lock:               # acquire #1
            self.deposit(amount)      # acquire #2 (same thread) -> OK with RLock
            self.deposit(amount)

acc = Account(100)
acc.deposit_twice(50)
print("balance after deposit_twice(50):", acc.balance)

# --- 2. A classic deadlock: two locks grabbed in opposite order ---
lock_a = Lock()
lock_b = Lock()

def worker_bad_1():
    with lock_a:
        time.sleep(0.05)
        # would then want lock_b -> but worker 2 holds it -> deadlock
        acquired = lock_b.acquire(timeout=0.2)
        if acquired:
            lock_b.release()
            print("worker_bad_1: got both locks")
        else:
            print("worker_bad_1: gave up (would have deadlocked)")

def worker_bad_2():
    with lock_b:
        time.sleep(0.05)
        acquired = lock_a.acquire(timeout=0.2)
        if acquired:
            lock_a.release()
            print("worker_bad_2: got both locks")
        else:
            print("worker_bad_2: gave up (would have deadlocked)")

t1 = Thread(target=worker_bad_1)
t2 = Thread(target=worker_bad_2)
t1.start(); t2.start()
t1.join(); t2.join()

# --- 3. The fix: always acquire locks in the SAME order ---
def worker_good(name):
    with lock_a:            # everyone takes A first...
        with lock_b:        # ...then B -> no circular wait, no deadlock
            print(f"{name}: safely holding both locks")

g1 = Thread(target=worker_good, args=("worker_good_1",))
g2 = Thread(target=worker_good, args=("worker_good_2",))
g1.start(); g2.start()
g1.join(); g2.join()
