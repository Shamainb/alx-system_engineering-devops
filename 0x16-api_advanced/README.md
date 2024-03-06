Task 0x16-api_advanced

0-subs.py
This script defines a function number_of_subscribers(subreddit) that queries the Reddit API and returns the number of subscribers for a given subreddit. If the subreddit is invalid, it returns 0.

1-top_ten.py
This script defines a function top_ten(subreddit) that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. If the subreddit is invalid, it prints None.

2-recurse.py
This script defines a recursive function recurse(subreddit, hot_list=[]) that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the subreddit, it returns None.

How to Use
Each script can be executed from the command line by passing the subreddit name as an argument.
