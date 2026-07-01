# 03 — Session auth vs token auth (concepts + mini demo)
# Run: python 03_session_vs_token.py

# Session: server stores state; browser sends session cookie
# Token (JWT): server is stateless; client sends Bearer token

SESSION_STORE: dict[str, dict] = {}


def login_session(username: str) -> str:
    import secrets

    session_id = secrets.token_urlsafe(16)
    SESSION_STORE[session_id] = {"username": username}
    return session_id


def get_user_from_session(session_id: str) -> str | None:
    return SESSION_STORE.get(session_id, {}).get("username")


def login_token(username: str) -> str:
    import os
    import time

    try:
        import jwt
    except ImportError:
        print("Install: pip install pyjwt")
        raise SystemExit(1)

    secret = os.getenv("JWT_SECRET", "change-me")
    return jwt.encode(
        {"username": username, "exp": int(time.time()) + 3600},
        secret,
        algorithm="HS256",
    )


if __name__ == "__main__":
    sid = login_session("alice")
    print("Session user:", get_user_from_session(sid))
    print("Token login:", login_token("bob")[:40], "...")
    print("\nUse sessions for classic web apps; JWT for APIs/mobile/SPAs.")
