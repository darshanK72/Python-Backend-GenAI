# 01 — Password hashing (never store plain passwords)
# Run: python 01_password_hashing.py
# Uses stdlib only

import hashlib
import secrets


def hash_password(password: str, salt: bytes | None = None) -> tuple[str, str]:
    salt = salt or secrets.token_bytes(16)
    key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000)
    return salt.hex(), key.hex()


def verify_password(password: str, salt_hex: str, key_hex: str) -> bool:
    salt = bytes.fromhex(salt_hex)
    _, new_key = hash_password(password, salt)
    return secrets.compare_digest(new_key, key_hex)


password = "my-secret-password"
salt_hex, key_hex = hash_password(password)
print("hash stored in DB:", key_hex[:32], "...")
print("verify OK:", verify_password(password, salt_hex, key_hex))
print("verify fail:", verify_password("wrong", salt_hex, key_hex))

print("\nIn production use: django.contrib.auth.hashers or passlib/bcrypt")
