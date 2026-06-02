# 06 — NumPy statistics
# Run: python 06_statistics.py

import numpy as np

scores = np.array([78, 85, 92, 88, 76, 95, 84])

print("mean:", np.mean(scores))
print("median:", np.median(scores))
print("std:", np.std(scores))
print("min/max:", np.min(scores), np.max(scores))
print("percentile 90:", np.percentile(scores, 90))

# --- 2. argmin / argmax ---
print("index of max:", np.argmax(scores))
print("top score:", scores[np.argmax(scores)])

# --- 3. Correlation ---
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
print("corrcoef:\n", np.corrcoef(x, y))
