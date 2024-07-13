#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""
import sys
from urllib import request, error

url = sys.argv[1]
try:
    with request.urlopen(url) as request:
        response = request.read().decode('utf-8')
        print(response)
except error.HTTPError as er:
        print('Erroe code:', er.code)
