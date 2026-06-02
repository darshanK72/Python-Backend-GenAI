# 01 — BeautifulSoup: parse HTML
# Run: python 01_parse_html.py
# Install: pip install beautifulsoup4

from bs4 import BeautifulSoup

html = """
<html>
  <head><title>Course Page</title></head>
  <body>
    <h1>Python Libraries</h1>
    <ul class="topics">
      <li>NumPy</li>
      <li>Pandas</li>
      <li>Requests</li>
    </ul>
    <a href="https://example.com">Read more</a>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# --- 1. Tags and text ---
print("title:", soup.title.string)
print("h1:", soup.h1.get_text())

# --- 2. find and find_all ---
for li in soup.find_all("li"):
    print("topic:", li.text)

link = soup.find("a", href=True)
print("link:", link["href"], link.text)

# --- 3. CSS selectors ---
items = soup.select("ul.topics li")
print("select:", [i.get_text(strip=True) for i in items])
