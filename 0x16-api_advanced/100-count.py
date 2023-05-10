#!/usr/bin/python3
"""
Function that queries the Reddit API
"""
import re
import requests
import sys


def append_title(dictionary, hot_posts):
    """ This function adds item into the list """
    if len(hot_posts) == 0:
        return

    t = hot_posts[0]['data']['title'].split()
    for w in t:
        for key in dictionary.keys():
            i = re.compile("^{}$".format(key), re.I)
            if i.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    append_title(dictionary, hot_posts)


def recurse_it(subreddit, dictionary, after=None):
    """ This function sends queries to the API """
    User_agent = 'MyRequest/0.1'
    headers = {'User-Agent': User_agent}
    params = {'after': after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if response.status_code != 200:
        return None

    diction = response.json()
    hot_posts = diction['data']['children']
    append_title(dictionary, hot_posts)
    after = diction['data']['after']
    if not after:
        return
    recurse_it(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ This function count words """
    dictionary = {}

    for w in w_list:
        dictionary[w] = 0

    recurse_it(subreddit, dictionary)

    ls = sorted(dictionary.items(), key=lambda kv: kv[1])
    ls.reverse()

    if len(ls) != 0:
        for i in l:
            if i[1] is not 0:
                print("{}: {}".format(i[0], i[1]))
    else:
        print("")
