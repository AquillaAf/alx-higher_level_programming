#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""
import urllib.request
import sys
var = len(sys.argv)
if var == 2:
    with urllib.request.urlopen(sys.argv[1]) as response:
        content = response.read()
        request_id = response.getheader('X-Request-Id')
        print(request_id)
else:
    print ("NO url provided")
