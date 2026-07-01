# 02 — JWT create and verify
# Run: python 02_jwt_basics.py
# Install: pip install pyjwt

import os
import time

try:
    import jwt
except ImportError:
    print("Install: pip install pyjwt")
    raise SystemExit(1)

SECRET = os.getenv("JWT_SECRET", "change-me-in-production")
ALGORITHM = "HS256"


def create_token(user_id: int, username: str, expires_in: int = 3600) -> str:
    payload = {
        "sub": str(user_id),
        "username": username,
        "exp": int(time.time()) + expires_in,
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    return jwt.decode(token, SECRET, algorithms=[ALGORITHM])


if __name__ == "__main__":
    token = create_token(42, "learner")
    print("Token (truncated):", token[:50], "...")
    claims = decode_token(token)
    print("Claims:", claims)
