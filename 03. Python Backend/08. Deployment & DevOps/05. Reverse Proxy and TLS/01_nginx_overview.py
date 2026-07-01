# 01 — Nginx reverse proxy overview
# Run: python 01_nginx_overview.py

NGINX_SNIPPET = """
upstream api_backend {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name api.example.com;

    location / {
        proxy_pass http://api_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
"""

if __name__ == "__main__":
    print("Nginx sits in front of Uvicorn/Gunicorn:")
    print("  - TLS termination (HTTPS)")
    print("  - Static files")
    print("  - Rate limiting and gzip\n")
    print("Example config:\n", NGINX_SNIPPET.strip())
