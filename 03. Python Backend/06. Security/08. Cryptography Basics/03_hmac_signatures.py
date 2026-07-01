# 03 — HMAC for message authentication
# Run: python 03_hmac_signatures.py

import hashlib
import hmac
import os

SECRET = os.getenv("HMAC_SECRET", "signing-secret-demo")


def sign(message: str) -> str:
    return hmac.new(SECRET.encode(), message.encode(), hashlib.sha256).hexdigest()


def verify(message: str, signature: str) -> bool:
    expected = sign(message)
    return hmac.compare_digest(expected, signature)


if __name__ == "__main__":
    msg = "order_id=1001&amount=49.99"
    sig = sign(msg)
    print("Signature:", sig)
    print("Valid:", verify(msg, sig))
    print("Modified:", verify(msg + "&hacked=1", sig))
