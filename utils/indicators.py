import ta

def add_indicators(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['Close']).rsi()
    df['macd'] = ta.trend.MACD(df['Close']).macd()
    df['sma'] = ta.trend.SMAIndicator(df['Close'], window=14).sma_indicator()
    df['ema'] = ta.trend.EMAIndicator(df['Close'], window=14).ema_indicator()
    return df
