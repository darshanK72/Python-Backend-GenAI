# 02 — Fetch page with requests + parse
# Run: python 02_scrape_with_requests.py
# Needs: pip install requests beautifulsoup4
# Needs: internet

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print("page title:", soup.title.string.strip())
print("first h1:", soup.find("h1").get_text(strip=True))
print("first paragraph:", soup.find("p").get_text(strip=True))

# Always check robots.txt and terms of service before scraping sites.
