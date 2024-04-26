#!/usr/bin/python3
"""
This script sends a POST request to a given URL with an 'email' as a parameter.
The script takes two command-line arguments: the URL and the email address.
It displays the body of the response, decoded in utf-8.
"""

import urllib.request
import urllib.parse
import sys


def send_email(url, email):

    """Sends a POST request to the URL with the email as a parameter."""
    data = {'email': email}
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=encoded_data)

    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)


if __name__ == "__main__":

    if len(sys.argv) > 2:
        send_email(sys.argv[1], sys.argv[2])
