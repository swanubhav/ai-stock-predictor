# 📈 AI Stock Predictor

An intelligent machine learning-based stock price prediction application that uses technical analysis indicators to forecast stock market movements. Built with Python, Streamlit, and scikit-learn.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30.0-red.svg)
![ML](https://img.shields.io/badge/ML-RandomForest-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🎯 Features

- **🌍 Multi-Market Support**
  - US Market stocks (NASDAQ, NYSE)
  - India NSE (National Stock Exchange)
  - India BSE (Bombay Stock Exchange)

- **📊 Technical Indicators**
  - **RSI (Relative Strength Index)** - Momentum analysis
  - **MACD (Moving Average Convergence Divergence)** - Trend identification
  - **SMA (Simple Moving Average)** - Price trend smoothing
  - **EMA (Exponential Moving Average)** - Recent price emphasis

- **🤖 Machine Learning**
  - Random Forest Classifier with 300 decision trees
  - Trained on 6 years of historical data (2018-2024)
  - Multi-stock training data (10 stocks: US tech + Indian stocks)
  - Binary classification: UP (1) or DOWN (0) prediction

- **💻 Interactive Web Interface**
  - Built with Streamlit for seamless user experience
  - Real-time stock data fetching
  - Interactive price trend visualization
  - Clean, centered UI layout

- **📈 Real-Time Data**
  - Fetches live stock data from Yahoo Finance
  - 6-month historical data analysis
  - Latest closing price display with currency conversion

---

## 📋 Table of Contents
ai-stock-predictor/
│
├── app.py                          # Main Streamlit web application
├── train_ml.py                     # Model training script
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── utils/                          # Utility modules
│   ├── __init__.py                # Package initialization
│   ├── indicators.py              # Technical indicator calculations
│   ├── market.py                  # Market and ticker formatting
│   └── sentiment.py               # Sentiment analysis (for future use)
│
├── models/                         # Trained models directory
│   └── stock_model.pkl            # Saved Random Forest model
│
└── data/                           # Data directory
    └── stock.csv                  # Sample stock data file
---
Detailed Process
Data Fetching:

Downloads historical stock data using Yahoo Finance API
Period: Last 6 months of daily data
Data includes: Open, High, Low, Close, Volume
Feature Engineering:

Calculates 4 technical indicators from closing prices
Each indicator has different properties for trend analysis
Market Formatting:

Converts stock symbols to exchange-specific format
US: "AAPL" → "AAPL" ($)
NSE: "reliance" → "RELIANCE.NS" (₹)
BSE: "reliance" → "RELIANCE.BO" (₹)
Prediction:

Uses the pre-trained Random Forest model
Inputs: Latest values of 4 technical indicators
Output: Binary classification (1 = UP, 0 = DOWN)
Visualization:

Shows latest stock price with currency
Displays prediction direction
Interactive line chart of price trends




