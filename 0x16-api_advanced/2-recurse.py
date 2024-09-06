import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API recursively and gathers titles of hot articles for a given subreddit.
    If the subreddit is invalid or no results are found, returns None.
    """
    base_url = "https://www.reddit.com/r/"
    headers = {"User-Agent": "MyRecursiveBot v1.0"}  # Our custom User-Agent, whispered to the Reddit guardians

    params = {"limit": 10, "after": after} if after else {"limit": 10}
    try:
        response = requests.get(f"{base_url}{subreddit}/hot.json", headers=headers, params=params)
        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            return None  # No posts found—perhaps the subreddit is a hidden treasure.
        else:
            hot_list.extend([post["data"]["title"] for post in posts])
            next_page = data["data"]["after"]
            if next_page:
                return recurse(subreddit, hot_list, after=next_page)
            else:
                return hot_list

    except (requests.RequestException, KeyError):
        return None
