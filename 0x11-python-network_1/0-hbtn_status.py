#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""
import urllib.request
url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    var = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(var)))
    print("\t- content: {}".format(var))
    print("\t- utf8 content: {}".format(var.decode('utf-8')))
