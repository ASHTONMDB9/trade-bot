import ccxt
import config

def connect_exchange():
    exchange = ccxt.binance({
        "apiKey": config.API_KEY,
        "secret": config.API_SECRET,
        "enableRateLimit": True
    })

    return exchange