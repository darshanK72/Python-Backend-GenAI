"""CLI shim for assignment spec — run: python kb_qa.py <question>"""

from app.cli.runner import main

# main - run the engineering KB Q&A CLI
if __name__ == "__main__":
    raise SystemExit(main())
