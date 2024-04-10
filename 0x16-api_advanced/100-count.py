#!/usr/bin/python3
"""Module for interacting with the Reddit API to retrieve information"""
from requests import get


REDDIT_URL = "https://www.reddit.com"
"""Base API URL for Reddit"""


def print_sorted_histogram(word_counts={}):
    '''Sorts and prints the given word counts histogram.
    '''
    word_counts = list(filter(lambda kv: kv[1], word_counts))
    word_counts_dict = {}
    for item in word_counts:
        if item[0] in word_counts_dict:
            word_counts_dict[item[0]] += item[1]
        else:
            word_counts_dict[item[0]] = item[1]
    word_counts = list(word_counts_dict.items())
    word_counts.sort(
        key=lambda kv: kv[0],
        reverse=False
    )
    word_counts.sort(
        key=lambda kv: kv[1],
        reverse=True
    )
    result_str = '\n'.join(list(map(
        lambda kv: '{}: {}'.format(kv[0], kv[1]),
        word_counts
    )))
    if result_str:
        print(result_str)


def count_words(subreddit, word_list, word_counts=[], cnt=0, after=None):
    """gets the count of given words found in hot posts of a subreddit"""
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
        f"{REDDIT_URL}/r/{subreddit}.json?sort={srt}&limit={lmt}"
        f"&count={cnt}&after={after if after else ''}",
        headers=reddit_headers,
        allow_redirects=False
    )
    if not word_counts:
        word_list = list(map(lambda word: word.lower(), word_list))
        word_counts = list(map(lambda word: (word, 0), word_list))
    if res_data.status_code == 200:
        data = res_data.json()['data']
        posts = data['children']
        titles = list(map(lambda post: post['data']['title'], posts))
        word_counts = list(map(
            lambda kv: (kv[0], kv[1] + sum(list(map(
                lambda txt: txt.lower().split().count(kv[0]),
                titles
            )))),
            word_counts
        ))
        if len(posts) >= lmt and data['after']:
            count_words(
                subreddit,
                word_list,
                word_counts,
                cnt + len(posts),
                data['after']
            )
        else:
            print_sorted_histogram(word_counts)
    else:
        return
