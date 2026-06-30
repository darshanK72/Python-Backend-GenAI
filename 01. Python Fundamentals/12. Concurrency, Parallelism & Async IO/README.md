# 07 — Concurrency, Parallelism & Async IO

Learn how to run many things at once in Python. Start with the core concepts,
then work through the three pillars in order: **threading** (concurrency for
I/O), **multiprocessing** (true parallelism for CPU work), and **asyncio**
(single-threaded concurrency for huge numbers of waits).

```bash
# from repo root
.venv\Scripts\activate

cd "01. Python Fundamentals/07. Advanced Topics/07. Concurrency, Parallelism & Async IO"
```

Every file is self-contained and runnable. Run them by name, in order.

## Files

| Order | File | Topic | How to run |
|-------|------|-------|------------|
| 01 | `01_concurrency_vs_parallelism.py` | Concepts: concurrency vs parallelism, I/O- vs CPU-bound | `python 01_concurrency_vs_parallelism.py` |
| | **Threading — concurrency for I/O-bound work** | | |
| 02 | `02_threading_basics.py` | `Thread(target=)`, subclassing, `join`, `is_alive` | `python 02_threading_basics.py` |
| 03 | `03_thread_arguments_and_daemon.py` | Passing args, collecting results, daemon threads | `python 03_thread_arguments_and_daemon.py` |
| 04 | `04_thread_lock.py` | Race conditions and `Lock` | `python 04_thread_lock.py` |
| 05 | `05_rlock_and_deadlock.py` | `RLock`, deadlocks and how to avoid them | `python 05_rlock_and_deadlock.py` |
| 06 | `06_event_and_condition.py` | `Event` and `Condition` signalling | `python 06_event_and_condition.py` |
| 07 | `07_semaphore.py` | `Semaphore` / `BoundedSemaphore` to limit concurrency | `python 07_semaphore.py` |
| 08 | `08_queue_communication.py` | `queue.Queue` producer/consumer pattern | `python 08_queue_communication.py` |
| 09 | `09_gil_explained.py` | The GIL, demonstrated (CPU vs I/O) | `python 09_gil_explained.py` |
| 10 | `10_thread_pool_executor.py` | `ThreadPoolExecutor`, futures, `as_completed` | `python 10_thread_pool_executor.py` |
| | **Multiprocessing — true parallelism for CPU-bound work** | | |
| 11 | `11_multiprocessing_basics.py` | `Process`, separate memory, real speedup | `python 11_multiprocessing_basics.py` |
| 12 | `12_multiprocessing_pool.py` | `Pool.map` / `starmap` over data | `python 12_multiprocessing_pool.py` |
| 13 | `13_process_communication.py` | `Queue`, `Pipe`, `Value`, `Array` | `python 13_process_communication.py` |
| 14 | `14_process_pool_executor.py` | `ProcessPoolExecutor` for parallel CPU work | `python 14_process_pool_executor.py` |
| | **Asyncio — single-threaded concurrency for I/O** | | |
| 15 | `15_asyncio_basics.py` | `async`/`await`, `asyncio.run`, `gather` | `python 15_asyncio_basics.py` |
| 16 | `16_asyncio_tasks_and_gather.py` | `create_task`, `gather`, `as_completed` | `python 16_asyncio_tasks_and_gather.py` |
| 17 | `17_asyncio_synchronization.py` | `asyncio.Lock` / `Semaphore` / `Queue` | `python 17_asyncio_synchronization.py` |
| 18 | `18_asyncio_timeouts_and_errors.py` | `wait_for`, cancellation, error handling | `python 18_asyncio_timeouts_and_errors.py` |
| 19 | `19_asyncio_run_in_executor.py` | Bridging blocking/CPU code with `run_in_executor` | `python 19_asyncio_run_in_executor.py` |
| | **Recap** | | |
| 20 | `20_choosing_the_right_tool.py` | Decision guide, comparison table, pitfalls | `python 20_choosing_the_right_tool.py` |

## Key ideas

- **Concurrency** = dealing with many tasks by taking turns. **Parallelism** =
  doing many tasks at the same instant on multiple cores.
- **I/O-bound** (waiting) vs **CPU-bound** (computing) is the question that
  decides which tool to reach for.
- **The GIL** lets only one thread run Python bytecode at a time, so threads
  don't speed up CPU work — but they're great while waiting on I/O.
- **`concurrent.futures`** gives one clean API (`ThreadPoolExecutor` /
  `ProcessPoolExecutor`); switching backends is often a one-line change.
- **asyncio** is cooperative: a task only yields at an `await`. Never block the
  event loop — offload blocking work with `run_in_executor` / `to_thread`.

## Cheat sheet

| Work type | Few tasks | Many tasks |
|-----------|-----------|------------|
| I/O-bound (waiting) | `threading` / `ThreadPoolExecutor` | `asyncio` |
| CPU-bound (computing) | `multiprocessing` / `ProcessPoolExecutor` | `multiprocessing` |

| | threading | multiprocessing | asyncio |
|--|-----------|-----------------|---------|
| Best for | I/O-bound | CPU-bound | massive I/O-bound |
| Memory | shared | separate | shared |
| GIL limit | yes | no (real parallelism) | n/a (one thread) |
| Switching | OS preemptive | OS / processes | cooperative (`await`) |

**Tip:** the multiprocessing lessons (11–14) must keep process-spawning code
under `if __name__ == "__main__":` or they'll misbehave on Windows and macOS.
