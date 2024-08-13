#!/usr/bin/python3

import json
import requests

USERNAME = 'Forward-Age6992'
CLIENT_ID = "5BXUX6gOYQJ8GzmvXZ6uUw"
SECRET = "Ic6OkjkdCEJ52Wp4DQuxUluKczP2Bg"
PASSWORD = '1010ilovelucibel'
# Request an OAuth Token from Reddit
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET)

#with open('passwd.txt', 'r') as f:
    #pw = f.read().strip()

data = {
        'grant_type': 'password',
        'username': USERNAME,
        'password': PASSWORD
        }

headers = {'User-Agent': 'MyRedditApp/0.1 by Forward-Age6992'}

# Send POST request to Reddit's OAuth2 token endpoint
response = requests.post('https://www.reddit.com/api/v1/access_token', auth=auth, data=data, headers=headers)

#response = response.json()

#check for success
if response.status_code != 200:
    print("Failed to aunthenticate", response.status_code, response.text)
    exit()

response = response.json()

token = response.get('access_token')
#print(token)
#print(response)

# we must add the token to our haeaders whenever we are using the Reddit API.
headers['Authorization'] = f'bearer {token}'

#print(headers)
# for ex to get my identity:
identity = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

if identity.status_code == 200:
    identity = identity.json()
    #print(json.dumps(identity, indent=2))

# retrieve the most popular posts in a subreddit
hot = requests.get('https://oauth.reddit.com/r/python/hot?limit=10', headers=headers)
hot = hot.json()
#print(json.dumps(hot, indent=4))
for post in hot.get('data').get('children'):
    print(post.get('data').get('title'))
