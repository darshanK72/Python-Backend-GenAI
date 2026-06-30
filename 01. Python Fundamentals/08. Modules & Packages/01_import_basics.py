# 01 — Importing modules
# Run: python 01_import_basics.py
# (run from this folder: 03 Modules)
#
# A module = any .py file. import loads and reuses its code.

# --- 1. import whole module ---
import math

print("pi =", math.pi)
print("sqrt(16) =", math.sqrt(16))

# --- 2. import with alias ---
import datetime as dt

now = dt.datetime.now()
print("now:", now.strftime("%Y-%m-%d %H:%M"))

# --- 3. from module import names ---
from math import floor, ceil

print("floor(3.7) =", floor(3.7), "ceil(3.2) =", ceil(3.2))

# --- 4. from module import * (avoid in production — pollutes namespace) ---
# from math import *

# --- 5. Local module in same folder ---
import demo_module

print(demo_module.greet("Darshan"))
print("PI =", demo_module.PI)
