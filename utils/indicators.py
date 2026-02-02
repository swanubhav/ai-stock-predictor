import ta

def add_indicators(df):
    if 'Close' not in df.columns:
        raise ValueError("DataFrame must contain 'Close' column")

    close = df['Close'].squeeze() 

    df['rsi'] = ta.momentum.RSIIndicator(close).rsi()

    macd = ta.trend.MACD(close)
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    df['macd_hist'] = macd.macd_diff()

    df['sma'] = ta.trend.SMAIndicator(close, window=14).sma_indicator()
    df['ema'] = ta.trend.EMAIndicator(close, window=14).ema_indicator()

    return df

