#!/usr/bin/python3
"""
This script takes a URL as a command-line argument and sends a GET request.
It displays the body of the response or prints an error code
if the HTTP status code is 400 or higher.
"""

import requests
import sys


def fetch_url(url):
    """Fetches content from a URL and handles HTTP status errors."""
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Errir code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fetch_url(sys.argv[1])
