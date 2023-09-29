#!/usr/bin/python3

"""Python script that fetches https://alx-intranet.hbtn.io/status."""

import requests
import sys


if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    request = requests.post(sys.argv[1], data=value)
    print(request.text)
