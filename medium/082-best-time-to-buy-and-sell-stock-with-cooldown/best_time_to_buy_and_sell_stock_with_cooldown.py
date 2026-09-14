class Solution:
    def max_profit(self, prices: list[int]) -> int:
        hold, sold, rest = float("-inf"), 0, 0  # best cash while holding / just sold / free to buy
        for price in prices:
            hold, sold, rest = max(hold, rest - price), hold + price, max(rest, sold)
        return max(sold, rest)
