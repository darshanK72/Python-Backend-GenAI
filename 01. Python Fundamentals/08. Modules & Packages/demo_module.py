# Helper module for import demos (do not run directly as main lesson).

PI = 3.14159
APP_NAME = "Learning Python"


def greet(name):
    return f"Hello, {name} from demo_module"


def _private_helper():
    return "internal use only"
