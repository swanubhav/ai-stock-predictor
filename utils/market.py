def format_ticker(symbol, market):
    symbol = symbol.upper().strip()

    if market == "India (NSE)":
        return symbol if symbol.endswith(".NS") else symbol + ".NS", "₹"
    elif market == "India (BSE)":
        return symbol if symbol.endswith(".BO") else symbol + ".BO", "₹"
    else:
        return symbol, "$"
