# 26 — Deployment and FastCGI (read-only)
# Run: python 26_deployment.py

# --- Development ---
#   python 03_hello.py
#   flask --app 03_hello run --debug --port 5000
# Never use debug=True in production.

# --- Production WSGI server ---
# Flask's built-in server is single-threaded and for learning only.
# Use Gunicorn (Linux/macOS) or Waitress (Windows-friendly):
#   pip install waitress
#   waitress-serve --port=5000 03_hello:app

# --- Gunicorn (Linux) ---
#   gunicorn -w 4 -b 0.0.0.0:5000 03_hello:app

# --- Reverse proxy ---
# Put Nginx or Caddy in front for HTTPS, static files, and load balancing.

# --- Environment ---
#   export FLASK_APP=app.py
#   export FLASK_ENV=production
# Store secrets (SECRET_KEY, DATABASE_URL) in environment variables.

# --- FastCGI (legacy) ---
# Older shared hosts used flup or WSGI-to-FastCGI bridges.
# Modern deployments use WSGI (Gunicorn/Waitress) behind a reverse proxy instead.

# --- Checklist ---
# [ ] DEBUG off, strong SECRET_KEY
# [ ] Use a production WSGI server
# [ ] HTTPS via reverse proxy
# [ ] Database migrations (Flask-Migrate / Alembic)

if __name__ == "__main__":
    print("Deploy Flask with Waitress/Gunicorn + HTTPS reverse proxy.")
    print("Practice project: see ../02. Notes API/app.py")
