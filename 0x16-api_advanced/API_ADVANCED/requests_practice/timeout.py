#!/usr/bin/python3

"""
You can tell Requests to stop waiting for a response after a given number of seconds by using the timeout param.
Nearly all production code shd use this param in nearly all requests.
If you dont, your program could hang indefinitely.
"""

import requests

r = requests.get('https://github.com', timeout=5) # timeout=0.01
print(r.status_code)

