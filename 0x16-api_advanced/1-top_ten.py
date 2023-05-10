#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "My API Agent"}
    params = {"limit": 10}
    res = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if res.status_code == 404:
        print("None")
        return
    data = res.json().get("data")
    [print(r.get("data").get("title")) for r in data.get("children")]
