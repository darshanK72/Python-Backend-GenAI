# 01 — Secure cookie flags
# Run: python 01_secure_cookie_flags.py

from http.cookies import SimpleCookie

cookie = SimpleCookie()
cookie["session_id"] = "abc123"
cookie["session_id"]["httponly"] = True
cookie["session_id"]["secure"] = True
cookie["session_id"]["samesite"] = "Lax"
cookie["session_id"]["path"] = "/"

if __name__ == "__main__":
    print("Set-Cookie header:")
    print(cookie.output(header="").strip())
    print("\nHttpOnly: JS cannot read cookie")
    print("Secure: sent only over HTTPS")
    print("SameSite: limits cross-site cookie sending")
