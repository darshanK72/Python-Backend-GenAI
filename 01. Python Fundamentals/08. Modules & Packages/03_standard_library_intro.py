# 03 — Standard library highlights
# Run: python 03_standard_library_intro.py
#
# Python ships with many modules — no pip install needed.

import random
import statistics
import os
import sys

# --- 1. random ---
nums = [random.randint(1, 6) for _ in range(5)]
print("dice rolls:", nums)
print("choice:", random.choice(["apple", "banana", "cherry"]))

# --- 2. statistics ---
data = [10, 20, 30, 40, 50]
print("mean:", statistics.mean(data))
print("median:", statistics.median(data))

# --- 3. os ---
print("cwd:", os.getcwd())
print("listdir (first 5):", os.listdir(".")[:5])

# --- 4. sys ---
print("python version:", sys.version.split()[0])
print("script name:", sys.argv[0])

# --- 5. Explore more: datetime, json, pathlib, collections, itertools ---
