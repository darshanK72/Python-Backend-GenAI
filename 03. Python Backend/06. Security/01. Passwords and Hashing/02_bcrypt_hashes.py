# 02 — bcrypt password hashes (production style)
# Run: python 02_bcrypt_hashes.py
# Install: pip install bcrypt

try:
    import bcrypt
except ImportError:
    print("Install: pip install bcrypt")
    raise SystemExit(1)


def hash_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))


def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)


if __name__ == "__main__":
    hashed = hash_password("learner-password")
    print("bcrypt hash:", hashed.decode()[:40], "...")
    print("Verify OK:", verify_password("learner-password", hashed))
    print("Verify fail:", verify_password("wrong", hashed))
