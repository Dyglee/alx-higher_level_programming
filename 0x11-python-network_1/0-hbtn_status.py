#!/usr/bin/python3
"""
Fetches and displays the status from ALX intranet status page using urllib.
"""

import urllib.request


def fetch_status():
    """Fetches the status from the ALX intranet status page."""
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content:", html.decode('utf-8'))


if __name__ == "__main__":
    fetch_status()
