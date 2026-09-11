from buy_sell import largest_proft

cases = [
    #(prices, expected)
    ([7, 1, 5, 3, 6, 4], 5),
    ([20, 10, 20, 11, 1, 20], 19)
]

def test_buy_sell(cases):
    for prices, expected in cases:
        result = largest_proft(prices)
        assert result == expected, f'{prices!r} -> FAIL. expected = {expected!r}, result = {result!r}'
        print(f'{prices!r} -> PASS')

test_buy_sell(cases)
