# 13 — Communicating between processes
# Run: python 13_process_communication.py
#
# Processes do NOT share memory, so a normal global won't work across them.
# Options to exchange data:
#   - Queue          : thread/process-safe message passing (most common)
#   - Pipe           : a two-way channel between exactly two processes
#   - Value / Array  : shared C-typed memory guarded by a lock

from multiprocessing import Process, Queue, Pipe, Value, Array
import time

# --- 1. Why a plain global fails across processes ---
shared_list = []   # each child gets its OWN copy; the parent's stays empty

def append_locally(x):
    shared_list.append(x)   # mutates the child's copy only

# --- 2. Queue: workers push results back to the parent ---
def worker(task, out_queue):
    time.sleep(0.1)
    out_queue.put((task, task * task))

# --- 3. Pipe: direct two-way conversation ---
def ping(conn):
    conn.send("ping")
    print("child received:", conn.recv())
    conn.close()

if __name__ == "__main__":
    # 1. demonstrate the no-sharing gotcha
    p = Process(target=append_locally, args=(42,))
    p.start(); p.join()
    print("parent's shared_list after child appended:", shared_list, "(still empty!)")
    print("-" * 40)

    # 2. Queue
    q = Queue()
    procs = [Process(target=worker, args=(i, q)) for i in range(4)]
    for pr in procs:
        pr.start()
    for pr in procs:
        pr.join()
    results = [q.get() for _ in range(4)]
    print("results via Queue:", sorted(results))
    print("-" * 40)

    # 3. Pipe
    parent_conn, child_conn = Pipe()
    pc = Process(target=ping, args=(child_conn,))
    pc.start()
    print("parent received:", parent_conn.recv())
    parent_conn.send("pong")
    pc.join()
    print("-" * 40)

    # 4. Shared memory: Value (single number) and Array (fixed sequence)
    counter = Value("i", 0)        # 'i' = C int
    numbers = Array("i", [0, 0, 0])

    def bump(counter, numbers):
        with counter.get_lock():   # guard the shared value
            counter.value += 1
        for idx in range(len(numbers)):
            numbers[idx] = idx * 10

    sp = Process(target=bump, args=(counter, numbers))
    sp.start(); sp.join()
    print("shared counter:", counter.value)
    print("shared array:", list(numbers))
