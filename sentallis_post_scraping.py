import praw
import json
import os
import yfinance as yf
from datetime import datetime, timedelta

# Initialize PRAW with your credentials
reddit = praw.Reddit(
    client_id="Jsg2t34JasVMvQkbv6KYBw",
    client_secret="D9Ok3OfqBqOx9RPqS_LWvbivyLTYYw",
    user_agent="ShayPatrickCormac01"
)

# Define the post ID (you can get this from the URL of the post)
post_id = '1h4ccah'  # Replace with the actual post ID

# Fetch the post using PRAW
post = reddit.submission(id=post_id)

# Extract the post details
post_texts = []
post.comments.replace_more(limit=0)  # To remove "MoreComments"
for comment in post.comments.list():
    post_texts.append(comment.body)

# Fetch stock data using yfinance
ticker = "STLA"  # Ticker for Stellantis
stock_data = yf.Ticker(ticker)

# Fetch the stock's historical data (for the last 2 days)
historical_data = stock_data.history(period="5d")
current_close = historical_data['Close'].iloc[-2]  # Most recent closing price
previous_close = historical_data['Close'].iloc[-1]  # Previous closing price
percentage_change = ((current_close - previous_close) / previous_close) * 100

# Get the current date
current_date = datetime.now().strftime('%Y-%m-%d')

# Calculate the next close date (5 business days later)
next_close_date = datetime.now() + timedelta(days=1)
next_close = next_close_date.strftime('%Y-%m-%d')

# Format the data
new_data = {
    "ticker": ticker,  
    "date": current_date,  
    "text": post_texts,
    "current_close": previous_close,
    "next_close": next_close,  
    "percentage_change": percentage_change
}

# Define the file path for the final training data
file_path = 'final_training_data1.json'

# Read the existing data (if the file exists)
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        existing_data = json.load(f)
else:
    existing_data = []

# Append the new data to the existing data
existing_data.append(new_data)

# Write the updated data back to the JSON file
with open(file_path, 'w') as f:
    json.dump(existing_data, f, indent=4)

print("Data successfully appended to final_training_data1.json")
