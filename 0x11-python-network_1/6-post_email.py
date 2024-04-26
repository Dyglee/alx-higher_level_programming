#!/usr/bin/python3
"""
This script takes a URL and an email address as command-line arguments.
It sends a POST request to the URL with the email as a parameter
and displays the body of the response.
"""

import requests
import sys


def send_post_request(url, email):
    """Sends a POST request with an email and prints the response body."""

    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)


if __name__ == "__main__":

    if len(sys.argv) > 2:
        send_post_request(sys.argv[1], sys.argv[2])
