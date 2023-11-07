#!/usr/bin/python3
"""
Queries Reddit API.
Prints the titles of first 10 hot posts for a gven subreddit.
"""
import requests


def top_ten(subreddit):
    """Function that queriis Reddit API"""
    if subreddit is None or type(subreddit) is not str:
        return print(None)

    url = f"http://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'a.quarshie'}

    params = {'limit': 10}
    try:
        response = requests.get(url, headers=headers, params=params).json()
        data = response['data']['children']
        for i in data:
            print(i['data']['title'])
    except Exception:
        return print(None)
