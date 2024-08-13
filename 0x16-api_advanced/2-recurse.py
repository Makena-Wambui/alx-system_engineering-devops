#!/usr/bin/python3

"""
Write a recursive function:
    Quries the REDDIT API to get a list of titles of all
    hot posts for a given subreddit.

    Pagination handled using after param.

    will handle cases where the subreddit is invalid or it has no results.

    """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Function: recurse

    Takes subreddit as main arg.

    optional arg: hot_list to store all titles of hot posts for the subreddit.

    optional arg: 'after' for handling pagination.
                   starts as None and is updated as you fetch more pages

    Returns: A list containing the titles of all hot posts,
             or None if subreddit is invalid.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditApp/0.1 by Forward-Age6992'}
    params = {'after': after, 'limit': 25}

    if subreddit:
        try:
            response = requests.get(url, params=params, headers=headers)

            # will raise exception for bad HTTP status code.
            response.raise_for_status()

            response = response.json()

            if 'data' in response and response['data']['children']:
                posts_list = response['data']['children']
                for post in posts_list:
                    post = post['data']['title']
                    hot_list.append(post)

            # get the after token to use in subsequent query
            after = response['data']['after']

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list

        except requests.exceptions.RequestException:
            return None
    else:
        return None
