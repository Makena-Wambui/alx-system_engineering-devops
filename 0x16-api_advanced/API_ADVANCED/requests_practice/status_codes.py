#!/usr/bin/python3


import requests

url = 'https://httpbin.org/get'
r = requests.get(url)

# To check the response status code:
# print(r.status_code)

# requests also has a builtin status code lookup object for easy reference
# print(r.status_code == requests.codes.ok)

"""
For bad requests:
    4xx client errors
        OR
    5xx server errors
We can raise it using Response.raise_for_status()

"""
bad = requests.get('https://httpbin.org/status/404')
# print(bad.status_code)

# bad.raise_for_status()

print(r.raise_for_status())
