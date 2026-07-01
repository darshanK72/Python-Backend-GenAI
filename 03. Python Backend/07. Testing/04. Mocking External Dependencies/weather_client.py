# External weather client — code under test

import requests


def fetch_temperature(city: str, api_key: str) -> float:
    url = f"https://api.example.com/weather/{city}"
    response = requests.get(url, params={"key": api_key}, timeout=5)
    response.raise_for_status()
    return float(response.json()["temp_c"])
