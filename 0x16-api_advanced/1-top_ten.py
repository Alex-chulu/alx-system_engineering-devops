#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 
    10 hot posts listed for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        
    Returns:
        None
    """
    url = "https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()["data"]["children"]

    for post in data:
        print(post["data"]["title"])

