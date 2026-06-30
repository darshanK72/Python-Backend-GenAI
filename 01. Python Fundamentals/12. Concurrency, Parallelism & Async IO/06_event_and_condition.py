# 06 — Event and Condition (signalling between threads)
# Run: python 06_event_and_condition.py
#
# Locks protect data. Event and Condition let threads WAIT for something.
#   - Event     : a simple on/off flag. Threads wait() until it is set().
#   - Condition : wait until a predicate becomes true, then get notified.

from threading import Thread, Event, Condition
import time

# --- 1. Event: one thread signals others to start ---
start_signal = Event()

def runner(name):
    print(f"{name}: waiting for the start signal")
    start_signal.wait()            # blocks until set() is called
    print(f"{name}: GO!")

runners = [Thread(target=runner, args=(f"runner-{i}",)) for i in range(3)]
for r in runners:
    r.start()

time.sleep(0.3)
print("referee: ready... set...")
start_signal.set()                 # wake up all waiting threads at once
for r in runners:
    r.join()
print("-" * 30)

# --- 2. Condition: producer/consumer with a shared list ---
condition = Condition()
items = []

def consumer():
    with condition:
        while not items:                       # guard against spurious wakeups
            print("consumer: nothing yet, waiting")
            condition.wait()                   # releases lock, sleeps, re-acquires
        print("consumer: got", items.pop(0))

def producer():
    time.sleep(0.3)
    with condition:
        items.append("widget")
        print("producer: produced a widget, notifying")
        condition.notify()                     # wake one waiting consumer

c = Thread(target=consumer)
p = Thread(target=producer)
c.start()
p.start()
c.join()
p.join()
