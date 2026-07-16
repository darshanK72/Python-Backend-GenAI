"""CLI shim for assignment spec — run: python brief_generator.py <topic>"""

from app.cli.runner import main

# main - run the technical brief generator CLI
if __name__ == "__main__":
    raise SystemExit(main())
