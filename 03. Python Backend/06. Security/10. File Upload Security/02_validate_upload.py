# 02 — Validate upload size and extension
# Run: python 02_validate_upload.py

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".pdf"}
MAX_BYTES = 2 * 1024 * 1024  # 2 MB


def validate_upload(filename: str, size: int, content_type: str) -> tuple[bool, str]:
    ext = "." + filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if ext not in ALLOWED_EXTENSIONS:
        return False, "extension not allowed"
    if size > MAX_BYTES:
        return False, "file too large"
    if content_type not in {"image/png", "image/jpeg", "application/pdf"}:
        return False, "content-type not allowed"
    return True, "ok"


if __name__ == "__main__":
    cases = [
        ("photo.png", 500_000, "image/png"),
        ("big.pdf", 5_000_000, "application/pdf"),
        ("script.exe", 1000, "application/octet-stream"),
    ]
    for name, size, ctype in cases:
        ok, reason = validate_upload(name, size, ctype)
        print(f"{name}: {ok} ({reason})")
