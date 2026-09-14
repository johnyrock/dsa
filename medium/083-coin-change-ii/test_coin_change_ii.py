import unittest
from coin_change_ii import Solution


class TestCoinChangeII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_change(self):
        cases = [
            # (amount, coins, expected)
            (5, [1, 2, 5], 4),            # 5, 2+2+1, 2+1+1+1, 1+1+1+1+1; swapped loops would give 9
            (3, [2], 0),                  # impossible
            (10, [10], 1),                # exactly one coin
            (0, [1, 2], 1),               # the empty combination
            (0, [7], 1),                  # amount 0 is 1 even when no coin fits
            (1, [2, 3], 0),               # every coin too large
            (4, [1, 2], 3),               # 2+2, 2+1+1, 1+1+1+1
            (5, [5, 2, 1], 4),            # coin order does not change the count
            (100, [1, 2, 5, 10], 2156),   # classic count, a bigger table
            (500, [3, 5, 7, 8, 9, 10, 11], 35502874),  # large answer, must not overflow or time out
        ]

        for amount, coins, expected in cases:
            with self.subTest(amount=amount, coins=coins):
                result = self.solution.change(amount, list(coins))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
