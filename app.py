import streamlit as st
import yfinance as yf
import pandas as pd
import joblib

from utils.indicators import add_indicators
from utils.market import format_ticker

st.set_page_config(page_title="AI Stock Predictor", layout="centered")
st.title("📈 AI-Based Global Stock Prediction System")

market = st.selectbox(
    "Select Market",
    ["US Market", "India (NSE)", "India (BSE)"]
)

symbol = st.text_input("Enter Stock Symbol", "AAPL")

if st.button("Predict"):
    ticker, currency = format_ticker(symbol, market)

    with st.spinner("Fetching stock data..."):
        df = yf.download(ticker, period="6mo")

    if df.empty:
        st.error("❌ Invalid ticker or no data found.")
    else:
        df = add_indicators(df)
        df.dropna(inplace=True)

        model = joblib.load("models/ml_model.pkl")

        X = df[['rsi', 'macd', 'sma', 'ema']].iloc[-1:]
        prediction = model.predict(X)[0]

        last_price = df['Close'].iloc[-1]

        st.subheader("📌 Prediction Result")
        st.metric("Latest Price", f"{currency}{last_price:.2f}")

        if prediction == 1:
            st.success("📈 Expected Direction: UP")
        else:
            st.error("📉 Expected Direction: DOWN")

        st.subheader("📊 Price Trend")
        st.line_chart(df['Close'])
