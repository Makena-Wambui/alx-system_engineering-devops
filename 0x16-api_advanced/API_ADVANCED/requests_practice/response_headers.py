#!/usr/bin/python3

import requests

"""
View the servers response headers
"""
r = requests.get('https://httpbin.org/get')

print(r.headers) # A python dict

"""
HTTP Header names are case insensitive.
"""

print(r.headers['CONTENT-TYPE'])
print(r.headers.get('content-type'))

"""
It is also special in that the server could have sent the same header multiple times
with different values,
but requests combines them so they can be represented in the dictionary within a single mapping.
"""
