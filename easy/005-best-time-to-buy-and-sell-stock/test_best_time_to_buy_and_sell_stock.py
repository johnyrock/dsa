from best_time_to_buy_and_sell_stock import max_profit


def test_max_profit():
    cases = [
        # (prices, expected)
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),           # only falls, never sell at a loss
        ([2, 4, 1], 2),                 # the low at the end is too late to use
        ([1], 0),                       # single day, cannot sell after buying
        ([3, 3, 3], 0),                 # flat prices, no profit
        ([1, 2], 1),                    # minimum length with a profit
        ([2, 1, 2, 1, 0, 1, 2], 2),     # minimum keeps dropping, best pair is 0 then 2
        ([3, 2, 6, 5, 0, 3], 4),        # best trade ends before the global minimum
    ]

    failures = 0
    for prices, expected in cases:
        result = max_profit(prices)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  prices={prices} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_max_profit()
