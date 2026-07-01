# 02 — XSS prevention: escape user input in HTML
# Run: python 02_xss_escaping.py

import html

user_comment = '<script>alert("xss")</script>'

unsafe_html = f"<p>{user_comment}</p>"
safe_html = f"<p>{html.escape(user_comment)}</p>"

if __name__ == "__main__":
    print("Unsafe HTML:", unsafe_html)
    print("Safe HTML:", safe_html)
    print("\nIn templates: Jinja2 auto-escapes by default; Django {{ }} escapes too.")
