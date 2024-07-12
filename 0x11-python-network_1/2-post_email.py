#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
import sys
import urllib.parse
import urllib.request

url = sys.argv[1]
data = {'email' : sys.argv[2]}
encoded = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url, data=encoded, method='POST')
with urllib.request.urlopen(request) as response:
    var = response.read().decode('utf-8')
    print(var)
