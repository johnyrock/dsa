import unittest
from koko_eating_bananas import Solution


class TestKokoEatingBananas(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_min_eating_speed(self):
        cases = [
            # (piles, h, expected)
            ([3, 6, 7, 11], 8, 4),               # the running example in the walkthrough
            ([30, 11, 23, 4, 20], 5, 30),        # h == len(piles): must eat the biggest pile in one hour
            ([30, 11, 23, 4, 20], 6, 23),        # one spare hour lets the 30 pile be split in two
            ([1], 1, 1),                         # single pile, minimum speed
            ([1000000000], 2, 500000000),        # one huge pile, exactly two hours
            ([3, 6, 7, 11], 100, 1),             # generous h: speed 1 already fits
            ([2, 2], 4, 1),                      # speed 1 uses every hour exactly
            ([312884470], 968709470, 1),         # h far larger than needed, still speed 1
            ([805306368, 805306368, 805306368], 1000000000, 3),  # floor division here would give 2
        ]

        for piles, h, expected in cases:
            with self.subTest(piles=piles, h=h):
                result = self.solution.min_eating_speed(piles, h)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
