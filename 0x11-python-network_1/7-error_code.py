#!/usr/bin/python3

"""Python script that fetches https://alx-intranet.hbtn.io/status."""

import requests
import sys


if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    if request.status_code >= 400:
        print(f"Error code: {request.status_code}")
    else:
        print(request.text)
