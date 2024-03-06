#!/usr/bin/python3
"""
a function that queries the Reddit API and prints the titles
"""

import requests

def top_ten(subreddit):
    # Reddit API endpoint for getting the hot posts of a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set a custom User-Agent to avoid potential issues
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    
    # Make the API request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the titles from the response
        try:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                print(title)
        except KeyError:
            print("Error: Unable to parse Reddit API response.")
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
    else:
        print(f"Error: Unable to fetch posts. Status code: {response.status_code}")
