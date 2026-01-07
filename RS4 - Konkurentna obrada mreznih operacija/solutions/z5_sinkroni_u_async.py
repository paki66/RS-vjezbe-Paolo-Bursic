"""
Sljedeći isječak programskog koda pretvorite u asinkroni program s konkurentnom obradom mrežnih zahtjeva:**

import requests

def fetch_url(url: str) -> str:
    response = requests.get(url, timeout=5)
    return response.text

def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com"
    ]

    for url in urls:
        content = fetch_url(url)
        print(f"Fetched {len(content)} characters from {url}")

if __name__ == "__main__":
    main()
"""