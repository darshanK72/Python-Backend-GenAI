# 02 — __name__ == "__main__"
# Run: python 02_name_main.py
#
# When a file is run directly, __name__ is "__main__".
# When imported, __name__ is the module name.

print("This file __name__ =", __name__)


def main():
    print("main() running")


if __name__ == "__main__":
    print("Executed as script")
    main()
else:
    print("Imported as module")

# Try: python 02_name_main.py
# Then in another file: import importlib; importlib.import_module("02_name_main")
