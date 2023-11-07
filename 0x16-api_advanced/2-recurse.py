#!/usr/bin/python3
"""
Recursive function that queries the Reddit API.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """queries reddit API"""
    if subreddit is None or type(subreddit) is not str:
        return None

    url = f'http://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'A. quarshie'}
    params = {
        'after': after,
        'limit': 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=True).json()
    if response.status_code == 404:
        return None

    data = response['data']
    after = data['after']
    count = data['dist']
    for item in data['children']:
        hot_list.append(item['data']['title'])

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
