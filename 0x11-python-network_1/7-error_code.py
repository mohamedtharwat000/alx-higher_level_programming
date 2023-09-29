#!/usr/bin/python3

"""
script that takes in a URL, sends a request to the URL and displays the
body of the response.
"""

import requests
import sys


if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    if request.status_code >= 400:
        print(f"Error code: {request.status_code}")
    else:
        print(request.text)
