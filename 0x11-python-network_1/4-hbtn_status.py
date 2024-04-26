#!/usr/bin/python3
"""
Fetches the status from 'https://alx-intranet.hbtn.io/status'
using the requests package and displays the body of the response.
"""
import requests


def fetch_status():
    """Fetches status using requests and prints formatted output."""

    response = requests.get('https://alx-intranet.hbtn.io/status')
    content = response.text

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)


if __name__ == "__main__":
    fetch_status()
