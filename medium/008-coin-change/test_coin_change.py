import unittest
from coin_change import Solution


class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_coin_change(self):
        cases = [
            # (coins, amount, expected)
            ([1, 2, 5], 11, 3),               # 5 + 5 + 1
            ([2], 3, -1),                     # impossible
            ([1], 0, 0),                      # zero amount, zero coins
            ([1], 2, 2),                      # only ones
            ([1, 3, 4], 6, 2),                # greedy would take 4 + 1 + 1 = 3 coins; 3 + 3 = 2 is right
            ([9, 6, 5, 1], 11, 2),            # greedy 9 + 1 + 1 = 3; 6 + 5 = 2
            ([2, 5, 10, 1], 27, 4),           # 10 + 10 + 5 + 2
            ([186, 419, 83, 408], 6249, 20),  # classic large case
            ([3, 7], 5, -1),                  # unreachable with both coins bigger than some gaps
            ([5], 5, 1),                      # exactly one coin
            ([2147483647], 2, -1),            # coin far larger than the amount
        ]

        for coins, amount, expected in cases:
            with self.subTest(coins=coins, amount=amount):
                result = self.solution.coin_change(list(coins), amount)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
