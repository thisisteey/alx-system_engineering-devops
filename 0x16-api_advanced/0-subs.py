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
                "AppleWebKit/537.36 (KHTML, like, Gecko)",
                "Chrome/97.0.4692.71",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.7.4)",
                "Safari/17.4.1"
            ])
    }
    res_data = get(
            f"{REDDIT_URL}/r/{subreddit}/about/.json",
            headers=reddit_headers,
            allow_redirects=False
    )
    if res_data.status_code == 200:
        return res_data.jso()["data"]["subscribers"]
    return 0
