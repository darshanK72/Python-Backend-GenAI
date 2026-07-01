# 02 — Caddy automatic HTTPS overview
# Run: python 02_caddy_overview.py

CADDYFILE = """
api.example.com {
    reverse_proxy 127.0.0.1:8000
}
"""

if __name__ == "__main__":
    print("Caddy auto-provisions TLS certificates (Let's Encrypt).")
    print("Minimal Caddyfile:\n", CADDYFILE.strip())
    print("\nGood for small deployments and local HTTPS experiments.")
