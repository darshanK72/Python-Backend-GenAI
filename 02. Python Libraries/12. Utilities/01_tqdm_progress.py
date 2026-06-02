# 01 — tqdm (progress bars)
# Run: python 01_tqdm_progress.py
# Install: pip install tqdm

from tqdm import tqdm
import time

# --- 1. Loop progress ---
for i in tqdm(range(20), desc="Processing"):
    time.sleep(0.05)

# --- 2. Manual update ---
total = 50
with tqdm(total=total, unit="item") as bar:
    for _ in range(total):
        time.sleep(0.02)
        bar.update(1)

print("done")
