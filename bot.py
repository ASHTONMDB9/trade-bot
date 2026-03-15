import time
import pandas as pd
import config
from exchange import connect_exchange
from arbitrage import find_triangular_opportunity
from trader import execute_trade

exchange = connect_exchange()

def get_prices():

    tickers = exchange.fetch_tickers()

    prices = {}

    for symbol in tickers:
        prices[symbol] = tickers[symbol]["last"]

    return prices


def run_bot():

    while True:

        prices = get_prices()

        opportunities = find_triangular_opportunity(
            prices,
            config.TRADE_AMOUNT
        )

        if opportunities:

            best = max(opportunities, key=lambda x: x["profit"])

            print("Opportunity found:", best)

            if config.AUTO_TRADE:

                pair1, pair2, pair3 = best["pairs"]

                execute_trade(exchange, pair1, "buy", config.TRADE_AMOUNT)
                execute_trade(exchange, pair2, "sell", config.TRADE_AMOUNT)
                execute_trade(exchange, pair3, "sell", config.TRADE_AMOUNT)

        time.sleep(5)