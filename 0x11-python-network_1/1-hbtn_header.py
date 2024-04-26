#!/usr/bin/python3
"""
This script takes a URL as a command-line argument, sends a request to the URL,
and displays the value of the 'X-Request-Id' header found in the response.
"""
import urllib.request
import sys


def fetch_x_request_id(url):
    """ fetche and print the x-request-id """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        fetch_x_request_id(sys.argv[1])
