# 02 — Webhook HMAC signature verification
# Run: python 02_webhook_hmac.py

import hashlib
import hmac
import json
import os

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "whsec_demo_change_me")


def sign_payload(body: bytes) -> str:
    digest = hmac.new(WEBHOOK_SECRET.encode(), body, hashlib.sha256).hexdigest()
    return f"sha256={digest}"


def verify_signature(body: bytes, header: str) -> bool:
    expected = sign_payload(body)
    return hmac.compare_digest(expected, header)


if __name__ == "__main__":
    payload = json.dumps({"event": "payment.completed", "id": 99}).encode()
    sig = sign_payload(payload)
    print("Signature:", sig)
    print("Valid:", verify_signature(payload, sig))
    print("Tampered:", verify_signature(b'{"event":"hack"}', sig))
