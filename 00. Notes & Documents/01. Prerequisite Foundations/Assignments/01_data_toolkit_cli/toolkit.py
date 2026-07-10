"""CLI shim for assignment spec — run: python toolkit.py <command>"""

from app.cli.runner import main

if __name__ == "__main__":
    raise SystemExit(main())
