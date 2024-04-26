#!/usr/bin/python3
"""
This script takes a URL as a command-line argument and sends a request.
It then displays the value of the 'X-Request-Id'
header found in the response.
"""
import requests
import sys


def fetch_x_request_id(url):
    """Fetches and prints the 'X-Request-Id' from the HTTP headers"""

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
    else:
        print("No'X-Request-Id' header found.")


if __name__ == "__main__":

    if len(sys.argv) > 1:
        fetch_x_request_id(sys.argv[1])
