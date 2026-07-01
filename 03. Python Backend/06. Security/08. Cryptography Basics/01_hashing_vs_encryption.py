# 01 — Hashing vs encryption
# Run: python 01_hashing_vs_encryption.py

import hashlib

PASSWORD = "learner-password"

if __name__ == "__main__":
    hashed = hashlib.sha256(PASSWORD.encode()).hexdigest()
    print("Hash (one-way):", hashed[:32], "...")
    print("Same input -> same hash:", hashlib.sha256(PASSWORD.encode()).hexdigest() == hashed)
    print("\nEncryption is reversible with a key (see 02_fernet_symmetric.py).")
    print("Use hashing for passwords; encryption for data you must read back.")
