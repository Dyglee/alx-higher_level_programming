#!/usr/bin/python3
"""
This script takes a URL as a command-line argument, sends a request to the URL,
and either displays the body of the response
or handles HTTP errors by displaying
the error code.
"""

import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """Fetches content from a URL, handling HTTP errors."""
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        fetch_url(sys.argv[1])
