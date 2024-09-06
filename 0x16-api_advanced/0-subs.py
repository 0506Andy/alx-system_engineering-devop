#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    base_url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "MyMagicalBot v1.0"}  # Set a custom User-Agent to avoid trouble with Too Many Requests

    try:
        response = requests.get(f"{base_url}{subreddit}/about.json", headers=headers)
        data = response.json()
        return data["data"]["subscribers"]
    except (requests.RequestException, KeyError):
        return 0

