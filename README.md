# Stock Movement Prediction using Sentiment Analysis on Reddit Posts

This project predicts stock price movement (up or down) by analyzing sentiment from Reddit posts, specifically the "WallStreetBets" subreddit. Sentiment scores are computed using TextBlob, and a simple neural network is used to classify stock movements based on these scores.

## Table of Contents
1. [Methodology](#methodology)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
5. [Results](#results)
6. [Contributing](#contributing)
7. [License](#license)

## Methodology

1. **Data Collection**:
   - Reddit posts dated **27-11-2024** are fetched using the **PRAW** library and Reddit API.
   - Posts and comments are preprocessed to exclude unnecessary numbers, URLs, and extra spacing.
   - **Tickers for companies** are extracted from posts and comments, and relevant comments for each company are saved into a JSON file.

2. **Stock Data Aggregation**:
   - Using the **yfinance** library, stock data such as current close values, next close values, and percentage change of stock values are fetched.
   - These stock data points are aggregated with the relevant comments and saved into a JSON file.

3. **Sentiment Analysis**:
   - The JSON file is loaded, and sentiment polarity scores are computed for the comments using **TextBlob**.
   - A stock movement indicator (`0` for down, `1` for up) is calculated based on the percentage change in stock value. This data is saved into another JSON file.

4. **Neural Network Construction**:
   - A simple neural network is implemented using **TensorFlow** and **Keras** to predict stock movement based on sentiment polarity scores and stock data.

## Technologies Used

- **Python**: Core language for scripting and implementation.
- **PRAW**: To scrape posts and comments from the "WallStreetBets" subreddit.
- **TextBlob**: For sentiment analysis and computing polarity scores.
- **yfinance**: To fetch historical stock data.
- **TensorFlow/Keras**: For building and training the neural network.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock-movement-prediction.git
   cd stock-movement-prediction
2. Install the dependacies
   ```bash
   pip install -r requirements.txt
3. Set up the Reddit API credentials:
   Create a praw.ini file with your Reddit API client credentials.   
