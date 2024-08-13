#!/usr/bin/python3

"""
A function that queries the Reddit API,
and returns the number of total subscribers for a given subreddit.
If an invalid subreddit is given, the function should return 0.

No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests,
ensure you’re setting a custom User-Agent.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers to a particular subreddit.

    If invalid subreddit, return 0.

    """
    try:
        base_url = 'https://www.reddit.com/r/'
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(
            base_url + '{}/about.json'.format(subreddit), headers=headers)
        return r.json().get('data').get('subscribers')
    except Exception:
        return 0
