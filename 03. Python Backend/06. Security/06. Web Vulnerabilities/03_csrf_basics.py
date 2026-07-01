# 03 — CSRF token pattern (double-submit style demo)
# Run: python 03_csrf_basics.py

import secrets

SESSION_CSRF: dict[str, str] = {}


def issue_csrf(session_id: str) -> str:
    token = secrets.token_urlsafe(32)
    SESSION_CSRF[session_id] = token
    return token


def validate_csrf(session_id: str, submitted: str) -> bool:
    expected = SESSION_CSRF.get(session_id)
    if not expected:
        return False
    import secrets as s

    return s.compare_digest(expected, submitted)


if __name__ == "__main__":
    sid = "session-abc"
    token = issue_csrf(sid)
    print("Valid POST:", validate_csrf(sid, token))
    print("Forged POST:", validate_csrf(sid, "fake-token"))
    print("\nFrameworks: Django {% csrf_token %}, Flask-WTF, FastAPI + session middleware.")
