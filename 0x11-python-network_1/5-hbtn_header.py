#!/usr/bin/python3

"""Python script that fetches https://alx-intranet.hbtn.io/status."""

import requests
import sys


if __name__ == "__main__":
    request = requests.get(sys.argv[1])
    print(request.headers.get("X-Request-Id"))
