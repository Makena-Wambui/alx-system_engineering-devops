#!/usr/bin/python3

"""
A function that queries the Reddit API,
and returns the number of total subscribers for a given subreddit.
If an invalid subreddit is given, the function should return 0.

No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests,
ensure you’re setting a custom User-Agent.
"""

import json
import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers to a particular subreddit.

    If invalid subreddit, return 0.

    """
    USERNAME = 'Forward-Age6992'
    CLIENT_ID = "5BXUX6gOYQJ8GzmvXZ6uUw"
    SECRET = "Ic6OkjkdCEJ52Wp4DQuxUluKczP2Bg"
    PASSWORD = '1010ilovelucibel'

    # Request an OAuth Token from Reddit
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET)

    # with open('passwd.txt', 'r') as f:
    # pw = f.read().strip()

    data = {
        'grant_type': 'password',
        'username': USERNAME,
        'password': PASSWORD
    }

    headers = {'User-Agent': 'MyRedditApp/0.1 by Forward-Age6992'}

    # url = 'https://www.reddit.com/r/gaming/about'
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyRedditApp/0.1 by Forward-Age6992'}

    if subreddit:
        try:
            response = requests.get(url,
                                    headers=headers, auth=auth,
                                    data=data, allow_redirects=False)

            response.raise_for_status()

            response = response.json()

            data = response.get('data')
            if data is None:
                return 0

            # if subscribers key does not exist, return 0
            subs = data.get('subscribers', 0)

            return subs

        except Exception:
            return 0
    else:
        return 0
