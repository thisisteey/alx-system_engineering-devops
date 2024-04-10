#!/usr/bin/python3
"""Module for interacting with the Reddit API to retrieve information"""
from requests import get


REDDIT_URL = "https://www.reddit.com"
"""Base API URL for Reddit"""


def number_of_subscribers(subreddit):
    """gets and returns the number of subscribers in a given subreddit"""
    reddit_headers = {
            "Accept": "application/json",
            "User-Agent": " ".join([
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.7.4)",
                "Firefox/124.0.2",
                "Safari/17.4.1"
            ])
    }
    res_data = get(
            f"{REDDIT_URL}/r/{subreddit}/about.json",
            headers=reddit_headers,
            allow_redirects=False
    )
    if res_data.status_code == 200:
        try:
            return res_data.json()["data"]["subscribers"]
        except KeyError:
            return 0
    elif res_data.status_code == 404:
        return 0
    else:
        return 0
