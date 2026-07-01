# 02 — Security response headers
# Run: python 02_security_headers.py

SECURITY_HEADERS = {
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Content-Security-Policy": "default-src 'self'",
}


def apply_headers(response_headers: dict) -> dict:
    updated = dict(response_headers)
    updated.update(SECURITY_HEADERS)
    return updated


if __name__ == "__main__":
    base = {"Content-Type": "application/json"}
    secured = apply_headers(base)
    print("Headers to send on every response:\n")
    for key, value in secured.items():
        print(f"  {key}: {value}")
