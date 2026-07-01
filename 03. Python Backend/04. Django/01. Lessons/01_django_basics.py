# 01 — Django basics (read-only)
# Run: python 01_django_basics.py

BASICS = """
Django is a batteries-included Python web framework.

Design philosophies:
  - DRY (Don't Repeat Yourself)
  - Explicit is better than implicit
  - Loose coupling between components

Advantages:
  - Built-in admin, ORM, auth, forms, templates
  - Secure defaults (CSRF, SQL injection protection via ORM)
  - Large ecosystem and documentation

History: Created at Lawrence Journal-World (2003), open-sourced 2005.
"""

if __name__ == "__main__":
    print(BASICS)
    print("Next: python 02_environment.py")
