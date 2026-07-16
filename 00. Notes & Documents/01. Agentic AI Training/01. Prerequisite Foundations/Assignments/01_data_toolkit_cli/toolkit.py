"""CLI shim for assignment spec — run: python toolkit.py <command>"""

from app.cli.runner import main

# main - run the data toolkit CLI
if __name__ == "__main__":
    raise SystemExit(main())
