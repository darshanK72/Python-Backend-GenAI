# 08 — queue.Queue (thread-safe producer/consumer)
# Run: python 08_queue_communication.py
#
# queue.Queue is the recommended way for threads to exchange data: it handles
# all the locking for you. Producers put() items; consumers get() them.
# This is the standard "work queue" pattern.

from threading import Thread
import queue
import time

work_queue = queue.Queue()
results = queue.Queue()

# --- 1. Producer: puts jobs onto the queue ---
def producer(num_jobs):
    for i in range(num_jobs):
        work_queue.put(i)
        print(f"produced job {i}")
        time.sleep(0.05)

# --- 2. Consumers: pull jobs, process them, mark them done ---
SENTINEL = None   # a "poison pill" tells a worker to stop

def consumer(name):
    while True:
        job = work_queue.get()       # blocks until an item is available
        if job is SENTINEL:
            work_queue.task_done()
            print(f"{name}: shutting down")
            break
        results.put(job * job)
        print(f"{name}: processed job {job}")
        work_queue.task_done()       # signal this item is fully handled

NUM_WORKERS = 2
consumers = [Thread(target=consumer, args=(f"worker-{i}",)) for i in range(NUM_WORKERS)]
for c in consumers:
    c.start()

prod = Thread(target=producer, args=(6,))
prod.start()
prod.join()

# --- 3. Wait for all work, then stop the workers ---
work_queue.join()                    # blocks until every task_done() is called
for _ in range(NUM_WORKERS):
    work_queue.put(SENTINEL)         # one poison pill per worker
for c in consumers:
    c.join()

collected = sorted(results.queue)
print("all results:", collected)
