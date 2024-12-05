import praw
import json
from datetime import datetime

# Reddit API authentication
reddit = praw.Reddit(
    client_id="Jsg2t34JasVMvQkbv6KYBw",
    client_secret="D9Ok3OfqBqOx9RPqS_LWvbivyLTYYw",
    user_agent="ShayPatrickCormac01"
)

# Function to fetch posts by date
def fetch_posts_by_date_iteratively(subreddit_name, target_date):
    target_timestamp = int(datetime.strptime(target_date, "%Y-%m-%d").timestamp())
    next_day_timestamp = target_timestamp + 86400  # Add 1 day in seconds

    subreddit = reddit.subreddit(subreddit_name)
    data = []
    last_post_timestamp = None

    while True:
        # Fetch posts starting after the last post timestamp
        posts = subreddit.new(limit=1000)
        found_posts = False

        for post in posts:
            post_timestamp = int(post.created_utc)

            # Skip if already processed
            if last_post_timestamp and post_timestamp >= last_post_timestamp:
                continue

            # Check if the post falls within the target date range
            if target_timestamp <= post_timestamp < next_day_timestamp:
                found_posts = True
                post_data = {
                    "title": post.title,
                    "score": post.score,
                    "url": post.url,
                    "timestamp": post.created_utc,
                    "comments": []
                }

                # Fetch comments
                post.comments.replace_more(limit=0)
                for comment in post.comments.list():
                    post_data["comments"].append(comment.body)

                data.append(post_data)

            # Update last post timestamp
            last_post_timestamp = post_timestamp

        if not found_posts:
            # If no new posts were found, break the loop
            break

    return data

# Fetch posts for the target date
target_date = "2024-11-27"
posts = fetch_posts_by_date_iteratively("WallStreetBets", target_date)

# Save the data to a JSON file
if posts:
    with open("reddit_stock_data_filtered.json", "w") as f:
        json.dump(posts, f, indent=4)
    print(f"Fetched {len(posts)} posts from {target_date} and saved to 'reddit_stock_data_filtered.json'")
else:
    print(f"No posts found for {target_date}")
