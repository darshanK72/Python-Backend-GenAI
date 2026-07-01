# 01 — Password hashing with PBKDF2 (stdlib)
# Run: python 01_password_hashing.py

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


if __name__ == "__main__":
    password = "my-secret-password"
    salt_hex, key_hex = hash_password(password)
    print("Stored hash (truncated):", key_hex[:32], "...")
    print("Verify OK:", verify_password(password, salt_hex, key_hex))
    print("Verify fail:", verify_password("wrong", salt_hex, key_hex))
