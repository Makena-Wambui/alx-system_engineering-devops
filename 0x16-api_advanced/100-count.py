#!/usr/bin/python3

"""
Write a recursive function:
    Queries the Reddit API for all hot articles/posts in a given subreddit.

    Counts occurrences of specific keywords
    in word_list param(case insensitive),
    so java is same as Java or JAvA in the titles of those posts.

    The results should be printed in a specific format:
        -> Words are printed in descending order of their count:
                => 25, 20, 18, 14, 4.....
        -> If two different words have the same count,
           for example, java and excel both appear 25 times in the titles,
           then they should be sorted alphabetically in ascending order.
           So excel should come first before java.
        -> If a particular word in word_list does not appear in the titles,
           then it should be skipped and not printed.
        -> These words should be printed in lower case.
        -> If no posts match or the subreddit is invalid, print nothing.
        -> "java!" or "java_" should not be counted as "java".
        -> If word_list contains duplicates i.e., ['java', 'Java'],
           then you need to ensure that the final count sums these duplicates.
"""

import requests
from collections import defaultdict as dd


def count_words(subreddit, word_list, after=None, counts=dd(int)):
    """
    Function: count_words

    Args:
        subreddit
        word_list
        after
        counts -> A dictionary to keep track of the count of each keyword.
    """

    # Normalize word_list to lowercase and handle duplicates
    normalized_word_list = [w.lower() for w in word_list]
    unique_words = set(normalized_word_list)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditApp/0.1 by Forward-Age6992'}
    params = {'limit': 25, 'after': after}

    if subreddit:
        try:
            response = requests.get(url, headers=headers, params=params)

            response.raise_for_status()

            response = response.json()

            data = response.get('data', {})

            posts_list = data.get('children', [])

            for post in posts_list:
                # return each title in lowercase
                title = post['data']['title'].lower()
                # split each title into a list of words
                title_words = title.split()

                for word in title_words:
                    word = word.strip('.,!?_"\'-:;')
                    if word in unique_words:
                        counts[word] += normalized_word_list.count(word)

            # retrieve after token
            after = data['after']

            if after:
                return count_words(subreddit, word_list, after, counts)

            if counts:
                # Sorting is done first by count in
                # descending order (-item[1]),
                # and then alphabetically by the word (item[0]).
                counts = sorted(counts.items(),
                                key=lambda item: (-item[1], item[0]))

                for word, count in counts:
                    print(f'{word}: {count}')

        except requests.exceptions.RequestException:
            return None
    else:
        return None

