import yfinance as yf
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from utils.indicators import add_indicators

# Multiple stocks for generalization
stocks = [
    "AAPL", "MSFT", "GOOGL", "AMZN",
    "TSLA", "META",
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS"
]

all_data = []

for ticker in stocks:
    df = yf.download(ticker, start="2018-01-01", end="2024-01-01")
    if df.empty:
        continue

    df = add_indicators(df)
    df['target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    df.dropna(inplace=True)
    all_data.append(df)

data = pd.concat(all_data)

X = data[['rsi', 'macd', 'sma', 'ema']]
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=True, random_state=42
)

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    random_state=42
)
model.fit(X_train, y_train)

joblib.dump(model, "models/stock_model.pkl")
print("✅ Generic stock prediction model trained & saved")


