#!/usr/bin/python3
"""function that retireves all users of a subreddit"""
import requests
import sys

subredditname = sys.argv[1]


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""

    if subreddit is None or type(subreddit) is not str:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        "User-Agent": "MyRedditApp/1.0"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    elif response.status_code == 302:
        return 0


if len(sys.argv) != 2:
    print("Usage: python script.py subreddit_name")
    sys.exit(1)

number_of_subscribers(subredditname)
