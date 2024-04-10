#!/usr/bin/python3
"""Module for interacting with the Reddit API to retrieve information"""
from requests import get


REDDIT_URL = "https://www.reddit.com"
"""Base API URL for Reddit"""


def count_words(subreddit, word_list, inst={}, after="", cnt=0):
    """gets the count of given words found in hot posts of a subreddit"""
    reddit_headers = {
            "Accept": "application/json",
            "User-Agent": " ".join([
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.7.4)",
                "Firefox/124.0.2",
                "Safari/17.4.1"
            ])
    }
    parms = {
        "after": after,
        "count": cnt,
        "limit": 100
    }
    res_data = get(
        f"{REDDIT_URL}/r/{subreddit}/hot.json",
        headers=reddit_headers,
        params=parms,
        allow_redirects=False
    )
    try:
        api_res = res_data.json()
        if res_data.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return
    api_data = api_res.get("data")
    after = api_data.get("after")
    cnt += api_data.get("dist")
    for post_data in api_data.get("children"):
        title_words = post_data.get("data").get("title").lower().split()
        for wrd in word_list:
            if wrd.lower() in title_words:
                wrd_occr = len([x for x in title_words if x == wrd.lower()])
                if inst.get(wrd) is None:
                    inst[wrd] = wrd_occr
                else:
                    inst[wrd] += wrd_occr
    if after is None:
        if len(inst) == 0:
            print("")
            return
        inst = sorted(inst.items(), key=lambda kv: (-kv[1], kv[0]))
        [print(f"{k}: {v}") for k, v in inst]
    else:
        count_words(subreddit, word_list, inst, after, cnt)
