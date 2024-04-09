#!/usr/bin/python3
"""Module for interacting with the Reddit API to retrieve information"""
from requests import get


REDDIT_URL = "https://www.reddit.com"
"""Base API URL for Reddit"""


def top_ten(subreddit):
    """gets and retrieves the title of the top ten posts of a subreddit"""
    reddit_headers = {
            "Accept": "application/json",
            "User-Agent": " ".join([
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.7.4)",
                "Firefox/124.0.2",
                "Safari/17.4.1"
            ])
    }
    srt = "top"
    lmt = 10
    res_data = get(
            f"{REDDIT_URL}/r/{subreddit}/.json?sort={srt}&limit={lmt}",
            headers=reddit_headers,
            allow_redirects=False
    )
    if res_data.status_code == 200:
        for post_item in res_data.json()["data"]["children"][0:10]:
            print(post_item["data"]["title"])
    else:
        print(None)
