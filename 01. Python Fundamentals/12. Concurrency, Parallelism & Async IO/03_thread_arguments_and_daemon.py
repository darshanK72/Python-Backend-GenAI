# 03 — Thread arguments, return values & daemon threads
# Run: python 03_thread_arguments_and_daemon.py
#
# Threads can't "return" a value directly, so we collect results another way.
# Daemon threads die automatically when the main program exits.

from threading import Thread
import time

# --- 1. Passing positional and keyword arguments ---
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

t = Thread(target=greet, args=("Asha",), kwargs={"greeting": "Hi"})
t.start()
t.join()

# --- 2. Collecting results from threads ---
# A thread's target return value is discarded. Write results into a shared
# container (each thread to its own slot, so no lock is needed here).
results = [None] * 3

def square_into(index, value):
    time.sleep(0.1)
    results[index] = value * value

threads = [Thread(target=square_into, args=(i, i + 1)) for i in range(3)]
for th in threads:
    th.start()
for th in threads:
    th.join()
print("collected results:", results)

# --- 3. Daemon threads (background helpers) ---
# A daemon thread won't keep the program alive. Use it for background work
# (heartbeats, log flushers) that should stop when the app stops.
def background_ticker():
    while True:
        print("  ...background tick...")
        time.sleep(0.2)

ticker = Thread(target=background_ticker, daemon=True)
ticker.start()

time.sleep(0.5)   # let it tick a few times
print("main work done; daemon thread will be killed on exit")
