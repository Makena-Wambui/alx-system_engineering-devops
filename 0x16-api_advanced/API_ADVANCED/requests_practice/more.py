#!/usr/bin/python3

"""
More complicated post requests.
Typically you want to send some form encoded data, much like an HTML form.
To achieve this, pass a dictionary to the data argument.

This dictionary of data will automatically be form encoded when the request is made.
"""
import json
import requests

data = {'key1': 'value1', 'key2': 'value2'}

"""
The dict passed to data can have multiple values for each key.
    By passing a list of  tuples, or a dict with lists as values.
"""

ttuples = [('key3', 'value3'), ('key3', 'value4')]

ddict = {'key3': ['value3', 'value4']}



r = requests.post('https://httpbin.org/post', data=data)
#print(r.text)

r1 = requests.post('https://httpbin.org/post', data=ttuples)
#print(r1.text)

r2 = requests.post('https://httpbin.org/post', data=ddict)
#print(r2.text)
#print(r1.text == r2.text)

"""
If you want to send data that is not form encoded,
Pass in a string instead of a dit to data.
That data will be posted directly.
The Github API/v3 accepts JSON-encoded POST/PATCH data:
    example below:
"""

url = 'https://httpbin.org/post'
url2 = 'https://api.github.com/events'
dataa = {'some': 'dict'}
d = 'my_data'

#res = requests.post(url, data=d)
h = {'Content-Type': 'application/json'}
ress = requests.post(url2, json.dumps(dataa), headers=h)
#print(ress.json())
"""
If you need the Content-Type Header set to application/json, and you do not want to encode the dict yourself,
You can pass the dict directly using json parameter,
and it will be automatically encoded.
json param is ignored if data or files params are passed.
"""

res2 = requests.post(url, json=dataa)
#print(res2.json())
#print(res.text)

"""
To upload/post multipart encoded files:
"""
#file = {'file': open('/bin/netstat', 'rb')}
#f = requests.post(url, files=file)
#print(f.text)

"""
You can set the filename, content_type and headers explicitly.
"""
#files = {'file': ('netstat', open('/bin/netstat', 'rb'), {'Expires': 0})}
#f = requests.post(url, files=files)
#print(f.text)

"""
If you want you can send strings to be received as files.

"""
f = {'file': ('my_file.txt', 'My name is Kendi\nI am from Carolina.\nI came here in 2019\n')}
response = requests.post(url, files=f)
print(response.text)
