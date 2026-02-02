import yfinance as yf
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from utils.indicators import add_indicators

# Download stock data (US stock for training)
ticker = "AAPL"
df = yf.download(ticker, start="2018-01-01", end="2024-01-01")

df.dropna(inplace=True)

# Add technical indicators
df = add_indicators(df)
df.dropna(inplace=True)

# Target: next-day price movement
df['target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
df.dropna(inplace=True)

X = df[['rsi', 'macd', 'sma', 'ema']]
y = df['target']

# Time-series split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, shuffle=False, test_size=0.2
)

# Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Evaluate
accuracy = accuracy_score(y_test, model.predict(X_test))
print("ML Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "models/ml_model.pkl")
print("ML model saved successfully.")

