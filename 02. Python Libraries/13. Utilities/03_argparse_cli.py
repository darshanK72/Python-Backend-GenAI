# 03 — argparse (command-line interfaces)
# Run: python 03_argparse_cli.py --name Darshan --count 3

import argparse

parser = argparse.ArgumentParser(description="Demo CLI tool")
parser.add_argument("--name", default="World", help="Name to greet")
parser.add_argument("--count", type=int, default=1, help="Times to repeat")
parser.add_argument("--verbose", action="store_true", help="Extra output")

args = parser.parse_args()

for i in range(args.count):
    msg = f"Hello, {args.name}!"
    if args.verbose:
        msg = f"[{i + 1}] {msg}"
    print(msg)
