#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts listed for a given subreddit.

    :param subreddit: str, the subreddit name
    """
    # Define the URL for the Reddit API endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Define the headers to be sent with the API request
    headers = {"User-Agent": "Mozilla/5.0"}

    # Make the API request and get the response data
    response = requests.get(url, headers=headers)

    # Check if the API request was successful
    if response.status_code == 200:
        # Extract the first 10 hot posts from the response data
        hot_posts = response.json()["data"]["children"][:10]

        # Print the titles of the first 10 hot posts
        for post in hot_posts:
            print(post["data"]["title"])
    else:
        print(None)

