#!/usr/bin/python3

"""
script that takes in a URL, sends a request to the URL and displays the body of
the response (decoded in utf-8).
"""

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
