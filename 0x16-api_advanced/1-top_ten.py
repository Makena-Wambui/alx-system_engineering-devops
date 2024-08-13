#!/usr/bin/python3

"""
A function that queries the Reddit API,
and prints the titles of the first 10 hot posts listed for a given subreddit.

Prototype: def top_ten(subreddit)
    If not a valid subreddit, print None.

Ensure that you are not following redirects.
"""

import requests


def top_ten(subreddit):
    """
    Func: top_ten

    Prints the titles of the first 10 hot posts for a given subreddit.
    """
    if subreddit:
        try:
            url = f'https://www.reddit.com/r/{subreddit}/hot.json'
            params = {'limit': 10}
            headers = {'User-Agent': 'MyRedditApp/0.1 by Forward-Age6992'}

            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()

            response = response.json()

            if 'data' in response and 'children' in response['data']:
                posts_list = response['data']['children']

                for post in posts_list:
                    print(post['data']['title'])
            else:
                print(None)

        except requests.exceptions.RequestException:
            print(None)

    else:
        print(None)
