#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of the hot articles (default: None).
        after (str): A token used to paginate through the API responses (default: None).
        
    Returns:
        list: A list containing the titles of all hot articles for the given subreddit,
    or None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    params = {"after": after} if after else {}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()["data"]["children"]

    for post in data:
        hot_list.append(post["data"]["title"])

    after = response.json()["data"]["after"]

    if after is not None:
        return recurse(subreddit, hot_list, after=after)
    else:
        return hot_list

