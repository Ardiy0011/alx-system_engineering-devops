#!/usr/bin/python3
"""
Contains a function that works with Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': '0x16-api_advanced:project:\
            v1.0.0 (by /u/Ajiboye Adeleye Pius)'}
    data = requests.get(url, headers=headers).json()
    try:
        subs = data["data"]["subscribers"]
        return subs
    except Exception:
        return 0
