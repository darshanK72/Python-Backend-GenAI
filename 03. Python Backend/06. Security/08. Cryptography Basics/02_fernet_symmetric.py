# 02 — Symmetric encryption with Fernet
# Run: python 02_fernet_symmetric.py
# Install: pip install cryptography

import os

try:
    from cryptography.fernet import Fernet
except ImportError:
    print("Install: pip install cryptography")
    raise SystemExit(1)

KEY = os.getenv("FERNET_KEY", Fernet.generate_key().decode()).encode()
fernet = Fernet(KEY)


def encrypt(plain: str) -> bytes:
    return fernet.encrypt(plain.encode())


def decrypt(token: bytes) -> str:
    return fernet.decrypt(token).decode()


if __name__ == "__main__":
    token = encrypt("sensitive-api-response")
    print("Ciphertext:", token[:40], b"...")
    print("Decrypted:", decrypt(token))
