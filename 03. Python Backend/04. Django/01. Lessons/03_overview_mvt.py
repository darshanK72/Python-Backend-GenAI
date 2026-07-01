# 03 — Overview and MVT pattern (read-only)
# Run: python 03_overview_mvt.py

MVT = """
MVC vs Django MVT:
  Model      -> database tables (models.py)
  View       -> business logic (views.py) — NOT the HTML template
  Template   -> HTML + Django Template Language
  URLconf    -> maps URLs to views (urls.py)

Django handles the "controller" role via URL routing + middleware.

Request flow:
  1. Browser hits a URL
  2. URLconf matches a view function or class
  3. View queries models if needed
  4. View renders a template (or returns JSON)
  5. Response sent to browser
"""

if __name__ == "__main__":
    print(MVT)
    print("Next: python 04_creating_project.py")
