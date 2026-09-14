import unittest
from best_time_to_buy_and_sell_stock_with_cooldown import Solution


class TestBestTimeToBuyAndSellStockWithCooldown(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_profit(self):
        cases = [
            # (prices, expected)
            ([1, 2, 3, 0, 2], 3),        # buy 1, sell 3, cooldown, buy 0, sell 2; without cooldown it would be 4
            ([1], 0),                    # one day, nothing to do
            ([2, 1], 0),                 # only falls, never buy
            ([1, 2], 1),                 # one round trip
            ([1, 2, 3], 2),              # hold through the rise, sell once
            ([1, 2, 4], 3),              # buy 1, sell 4
            ([1, 4, 2], 3),              # sell at the peak, ignore the drop
            ([6, 1, 3, 2, 4, 7], 6),     # buy 1, sell 7 beats splitting because of the cooldown
            ([1, 2, 3, 4, 5], 4),        # monotone rise, one trade
            ([5, 4, 3, 2, 1], 0),        # monotone fall, no trade
            ([2, 1, 4, 5, 2, 9, 7], 10),  # buy 1 sell 4, cooldown, buy 2 sell 9; selling at 5 blocks the buy at 2
            ([3, 3, 3], 0),              # flat, no profit
        ]

        for prices, expected in cases:
            with self.subTest(prices=prices):
                result = self.solution.max_profit(list(prices))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
