# Auth helper — code under test

import secrets

VALID_KEYS = {"demo-key"}


def is_authorized(header_value: str) -> bool:
    return any(secrets.compare_digest(header_value, key) for key in VALID_KEYS)


def protected_action(user_key: str) -> dict:
    if not is_authorized(user_key):
        raise PermissionError("unauthorized")
    return {"message": "secret data"}
