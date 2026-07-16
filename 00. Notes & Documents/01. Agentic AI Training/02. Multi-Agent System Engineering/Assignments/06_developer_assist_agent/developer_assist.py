"""CLI shim for assignment spec — run: python developer_assist.py <question>"""

from app.cli.runner import main

# main - run the developer assist CLI
if __name__ == "__main__":
    raise SystemExit(main())
