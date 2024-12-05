# Stock Movement Prediction using Sentiment Analysis on Reddit Posts

This project predicts stock price movement (up or down) by analyzing sentiment from Reddit posts, specifically the "wallstreetbets" subreddit. Sentiment scores are computed using TextBlob, and a simple neural network is used to classify stock movements based on these scores.

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
- **PRAW**: To scrape posts and comments from the "wallstreetbets" subreddit.
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
   ```bash
   [DEFAULT]
      client_id=your_client_id
      client_secret=your_client_secret
      user_agent=your_user_agent
4. Fetch Reddit posts and comments.
5. Train the neural network.

## Usage

1. To scrape Reddit posts and generate sentiment polarity scores, run the appropriate scripts sequentially.
2. Use the trained model to predict stock movements for a company:
   ```bash
   from tensorflow.keras.models import load_model
   model = load_model('sentiment_stock_model.h5')
   predictions = model.predict(input_data)

## Results
The neural network predicts whether a stock will move up or down based on sentiment polarity scores and stock data. Example outputs include:
1. Input: Sentiment scores for company X and previous close value.
2. Output: Stock movement prediction (0 for down, 1 for up).

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-name).
3. Commit your changes (git commit -m "Add feature-name").
4. Push to the branch (git push origin feature-name).
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Batman12456/stock-movement-prediction/blob/main/LICENSE) file for details.
