#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept..
curl -si -X OPTIONS "${1}" | grep -oP 'Allow:\s*\K.*' | sed 's/Allow: //'
