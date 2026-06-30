# 20 — Choosing the right tool (decision guide & recap)
# Run: python 20_choosing_the_right_tool.py
#
# A single page tying the whole folder together. Two questions decide almost
# everything:
#   Q1: Is the work I/O-bound (waiting) or CPU-bound (computing)?
#   Q2: How many tasks — a handful, or hundreds/thousands?

GUIDE = """
=========================================================================
                    CONCURRENCY DECISION GUIDE
=========================================================================

Is your work mostly WAITING (network, disk, DB) or COMPUTING (math, parsing)?

  WAITING  (I/O-bound)
  ---------------------------------------------------------------------
  A few dozen tasks      -> threading / ThreadPoolExecutor   (lessons 02-10)
  Hundreds / thousands   -> asyncio                          (lessons 15-19)
                            (needs async-aware libraries, e.g. aiohttp)

  COMPUTING (CPU-bound)
  ---------------------------------------------------------------------
  Heavy pure-Python math -> multiprocessing / ProcessPool    (lessons 11-14)
                            (sidesteps the GIL, uses all cores)

  MIXED
  ---------------------------------------------------------------------
  Async app that must call blocking/CPU code
                         -> run_in_executor / to_thread       (lesson 19)

=========================================================================
                         QUICK COMPARISON
=========================================================================

                | threading      | multiprocessing | asyncio
----------------+-----------------+-----------------+------------------
 Good for       | I/O-bound       | CPU-bound       | massive I/O-bound
 Runs in        | 1 process,      | many processes, | 1 process,
                | many threads    | 1+ thread each  | 1 thread
 Memory         | shared          | separate        | shared
 Limited by GIL | yes (no CPU     | no (true        | n/a (single
                | parallelism)    | parallelism)    | thread)
 Switching      | OS preemptive   | OS / processes  | cooperative (await)
 Overhead       | low             | high (spawn)    | very low
----------------+-----------------+-----------------+------------------

=========================================================================
                          COMMON PITFALLS
=========================================================================
 * Using threads for CPU-bound code -> the GIL means no speedup (lesson 09).
 * Forgetting `if __name__ == '__main__':` -> multiprocessing breaks on
   Windows/macOS (lessons 11-14).
 * Calling time.sleep() or blocking calls inside a coroutine -> freezes the
   whole event loop; offload it instead (lesson 19).
 * Sharing mutable state without a Lock -> race conditions (lesson 04).
 * Acquiring multiple locks in different orders -> deadlock (lesson 05).
"""

if __name__ == "__main__":
    print(GUIDE)
