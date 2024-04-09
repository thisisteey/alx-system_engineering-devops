#!/usr/bin/python3
"""Module for interacting with the Reddit API to retrieve information"""
from requests import get


REDDIT_URL = "https://www.reddit.com"
"""Base API URL for Reddit"""


def recurse(subreddit, hot_list=[], cnt=0, after=None):
    """gets and retrieves the list of hot posts of a subreddit"""
    reddit_headers = {
            "Accept": "application/json",
            "User-Agent": " ".join([
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.7.4)",
                "Firefox/124.0.2",
                "Safari/17.4.1"
            ])
    }
    srt = "hot"
    lmt = 30
    res_data = get(
        f"{REDDIT_URL}/r/{subreddit}.json?sort={srt}&limit={lmt}&"
        f"count={cnt}&after={after if after else ''}",
        headers=reddit_headers,
        allow_redirects=False
    )
    if res_data.status_code == 200:
        data = res_data.json()["data"]
        posts = data["children"]
        pst_cnt = len(posts)
        hot_list.extend(list(map(lambda x: x["data"]["title"], posts)))
        if pst_cnt >= lmt and data["after"]:
            return recurse(subreddit, hot_list, cnt + pst_cnt, data["after"])
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None
