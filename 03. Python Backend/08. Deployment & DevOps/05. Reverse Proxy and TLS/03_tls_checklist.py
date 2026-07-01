# 03 — TLS and proxy headers checklist
# Run: python 03_tls_checklist.py

CHECKLIST = [
    "Terminate TLS at reverse proxy (Nginx/Caddy/ALB)",
    "Redirect HTTP -> HTTPS",
    "Set HSTS header in production",
    "Forward X-Forwarded-Proto so app knows HTTPS",
    "Run app on 127.0.0.1, not public interface directly",
    "Use --proxy-headers with Uvicorn behind proxy",
]

if __name__ == "__main__":
    print("Production TLS checklist:\n")
    for i, item in enumerate(CHECKLIST, 1):
        print(f"  {i}. {item}")
