import config

def calculate_profit(a, b, c, start):
    step1 = start / a
    step2 = step1 * b
    final = step2 * c

    profit = final - start
    percent = profit / start

    return percent, final


def find_triangular_opportunity(prices, start_amount):

    opportunities = []

    for pair1 in prices:
        for pair2 in prices:
            for pair3 in prices:

                try:
                    p1 = prices[pair1]
                    p2 = prices[pair2]
                    p3 = prices[pair3]

                    profit, final = calculate_profit(p1, p2, p3, start_amount)

                    if profit > config.MIN_PROFIT:
                        opportunities.append({
                            "pairs": (pair1, pair2, pair3),
                            "profit": profit,
                            "final": final
                        })

                except:
                    pass

    return opportunities