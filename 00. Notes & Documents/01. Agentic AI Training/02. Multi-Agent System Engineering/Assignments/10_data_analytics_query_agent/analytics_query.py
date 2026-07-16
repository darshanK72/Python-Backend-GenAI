"""CLI shim for assignment spec — run: python analytics_query.py <question>"""

from app.cli.runner import main

# main - run the analytics query CLI
if __name__ == "__main__":
    raise SystemExit(main())
