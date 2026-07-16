"""CLI shim for assignment spec — run: python prompt_toolkit.py"""

from app.cli.runner import main

# main - run the prompt engineering toolkit CLI
if __name__ == "__main__":
    raise SystemExit(main())
