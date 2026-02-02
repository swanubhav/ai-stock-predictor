import streamlit as st
import yfinance as yf
import joblib
from utils.indicators import add_indicators
from utils.market import format_ticker

st.set_page_config(page_title="AI Stock Predictor", layout="centered")
st.title("📈 AI-Based Stock Prediction App")

market = st.selectbox(
    "Select Market",
    ["US Market", "India (NSE)", "India (BSE)"]
)

symbol = st.text_input("Enter Stock Symbol", "AAPL")

if st.button("Predict"):
    ticker, currency = format_ticker(symbol, market)

    df = yf.download(ticker, period="6mo")

    if df is None or df.empty:
        st.error("No data found. Check stock symbol.")
        st.stop()

    df = add_indicators(df)
    df.dropna(inplace=True)

    try:
        model = joblib.load("models/stock_model.pkl")
    except:
        st.error("Model file missing.")
        st.stop()

    latest = df[['rsi', 'macd', 'sma', 'ema']].iloc[-1:]
    prediction = model.predict(latest)[0]

    last_price = df['Close'].iloc[-1]

    st.subheader("📌 Prediction Result")
    st.text(f"Latest Price: {currency}{last_price:.2f}")

    if prediction == 1:
        st.success("📈 Expected Direction: UP (Next Day)")
    else:
        st.error("📉 Expected Direction: DOWN (Next Day)")

    st.subheader("📊 Recent Price Trend")
    st.line_chart(df['Close'])

