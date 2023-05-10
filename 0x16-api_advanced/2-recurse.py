#!/usr/bin/python3
"""a recursive function that queries the Reddit API """
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing 
    the titles of all hot articles for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list, optional): A list to store the hot article titles. 
        Defaults to None.
        after (str, optional): A parameter to specify the starting point 
        of the next page of results. Defaults to None.
        
    Returns:
        list: A list containing the titles of all hot articles for the given 
        subreddit. Returns None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []
        
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", "after": after}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data").get("children")
    after = response.json().get("data").get("after")
    
    for post in data:
        hot_list.append(post.get("data").get("title"))
        
    if after is not None:
        recurse(subreddit, hot_list, after)
    
    return hot_list
