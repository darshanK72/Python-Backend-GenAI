# 03 — Preprocessing with sklearn
# Run: python 03_preprocessing.py

import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# --- 1. StandardScaler (mean 0, std 1) ---
data = np.array([[1000], [2000], [3000], [4000], [5000]], dtype=float)
scaler = StandardScaler()
scaled = scaler.fit_transform(data)
print("scaled:\n", scaled)

# --- 2. LabelEncoder for categories ---
le = LabelEncoder()
labels = le.fit_transform(["low", "high", "medium", "low"])
print("encoded:", labels)
print("classes:", le.classes_)

# --- 3. Inverse transform ---
print("restored:", le.inverse_transform([0, 2, 1]))
