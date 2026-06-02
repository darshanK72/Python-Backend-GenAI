# 10 — Combining *args and **kwargs
# Run: python 10_args_and_kwargs_together.py
#
# Full parameter order:
#   def f(pos1, pos2, /, pos_or_kw, *, kw_only, **kwargs)
# Simpler common form:
#   def f(required, *args, default=0, **kwargs)

def demo(a, b, *args, default="x", **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("default =", default)
    print("kwargs =", kwargs)

demo(1, 2, 3, 4, default="y", city="Nashik", age=25)

# --- Practical: flexible logger ---
def log(message, *tags, level="INFO", **meta):
    tag_str = " ".join(f"[{t}]" for t in tags)
    meta_str = " ".join(f"{k}={v}" for k, v in meta.items())
    print(f"{level}: {tag_str} {message} {meta_str}".strip())

log("Server started", "app", "v1", level="DEBUG", port=8080)

# --- Forwarding all arguments ---
def wrapper(*args, **kwargs):
    print("calling with", args, kwargs)
    return sum(args)

print("wrapper(1, 2, 3) =", wrapper(1, 2, 3))
