#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and returns a list
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    if 'data' not in data or 'children' not in data['data']:
        return None

    children = data['data']['children']
    for child in children:
        hot_list.append(child['data']['title'])

    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
