import config

def execute_trade(exchange, pair, side, amount):

    try:
        order = exchange.create_market_order(
            pair,
            side,
            amount
        )

        return order

    except Exception as e:
        print("Trade failed:", e)
        return None