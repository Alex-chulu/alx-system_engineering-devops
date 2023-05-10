#!/usr/bin/python3
"""function that queries the Reddit API 
then returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit. 
        Returns 0 if the subreddit is invalid.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My API Request Agent'}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        data = res.json()
        return data.get('data').get('subscribers')
    else:
        return 0
