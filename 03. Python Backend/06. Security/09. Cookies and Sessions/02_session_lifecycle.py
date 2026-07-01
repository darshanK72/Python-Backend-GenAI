# 02 — Session lifecycle (create, rotate, invalidate)
# Run: python 02_session_lifecycle.py

import secrets
import time

SESSIONS: dict[str, dict] = {}
SESSION_TTL = 3600


def create_session(user_id: int) -> str:
    session_id = secrets.token_urlsafe(32)
    SESSIONS[session_id] = {"user_id": user_id, "created": time.time()}
    return session_id


def get_session(session_id: str) -> dict | None:
    data = SESSIONS.get(session_id)
    if not data:
        return None
    if time.time() - data["created"] > SESSION_TTL:
        SESSIONS.pop(session_id, None)
        return None
    return data


def rotate_session(old_id: str) -> str | None:
    data = get_session(old_id)
    if not data:
        return None
    SESSIONS.pop(old_id, None)
    return create_session(data["user_id"])


def logout(session_id: str) -> None:
    SESSIONS.pop(session_id, None)


if __name__ == "__main__":
    sid = create_session(42)
    print("Active:", get_session(sid))
    new_sid = rotate_session(sid)
    print("Rotated:", new_sid is not None)
    print("Old invalid:", get_session(sid))
    logout(new_sid)
    print("After logout:", get_session(new_sid))
