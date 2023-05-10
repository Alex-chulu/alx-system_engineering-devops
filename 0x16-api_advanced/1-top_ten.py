#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    headers = {'User-Agent': 'MyApi'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for result in results:
            print(data.get('data').get('title'))
    else:
        print(None)
