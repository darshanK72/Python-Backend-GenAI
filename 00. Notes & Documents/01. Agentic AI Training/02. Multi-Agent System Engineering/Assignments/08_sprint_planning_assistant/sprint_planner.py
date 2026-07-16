"""CLI shim for assignment spec — run: python sprint_planner.py <request>"""

from app.cli.runner import main

# main - run the sprint planning assistant CLI
if __name__ == "__main__":
    raise SystemExit(main())
