# 01 — Iterators and iter()
# Run: python 01_iterators.py
#
# Iterable: can be looped (list, str, dict)
# Iterator: object with __iter__() and __next__()

nums = [10, 20, 30]
it = iter(nums)

print(next(it))
print(next(it))
print(next(it))
# print(next(it))   # Uncomment -> StopIteration

# --- 1. for-loop uses iter/next internally ---
for n in nums:
    print(n, end=" ")
print()

# --- 2. Custom iterator class ---
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for n in Countdown(5):
    print(n, end=" ")
print()
