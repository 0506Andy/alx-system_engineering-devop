#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    base_url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "MyMagicalBot v1.0"}  # Set a custom User-Agent to avoid trouble with Too Many Requests

    try:
        response = requests.get(f"{base_url}{subreddit}/hot.json?limit=10", headers=headers)
        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            print("No posts found. Perhaps the subreddit is a hidden treasure.")
        else:
            print(f"Top 10 hot posts in r/{subreddit}:\n")
            for post in posts:
                print(post["data"]["title"])

    except (requests.RequestException, KeyError):
        print("None")  # Invalid subreddit or mystical interference—either way, we return None.
