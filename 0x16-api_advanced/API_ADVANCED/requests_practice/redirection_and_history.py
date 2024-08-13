#!/usr/bin/python3

"""
By default, Requests will perform local redirection for all verbs except HEAD.
Use the history property of the Response object to track redirection

Response.history list contains Response objects that were created so as to complete the request.
This list is sorted from oldest to most recent response.
Example:
    Github redirects all HTTP requests to HTTPS
"""

import requests

r = requests.get('http://github.com')

print(r.url)

print(r.status_code)

print(r.history[0])

"""
If using GET, POST, PUT, DELETE, OPTIONS, PATCH,
You can disable redirection handling using the allow_redirects param.
"""

r = requests.get('http://github.com', allow_redirects=False)

print(r.status_code)

print(r.history)

"""
If using HEAD, you can enable redirection:
"""
r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)

r = requests.head('http://github.com')
print(r.status_code)

r = requests.head('http://github.com', allow_redirects=True)
print(r.status_code)
print(r.url)
print(r.history)
