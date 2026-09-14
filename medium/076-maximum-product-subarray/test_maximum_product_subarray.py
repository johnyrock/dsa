import unittest
from maximum_product_subarray import Solution


class TestMaximumProductSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_product(self):
        cases = [
            # (nums, expected)
            ([2, 3, -2, 4], 6),          # the running example: [2, 3]
            ([-2, 0, -1], 0),            # the zero is the best on offer; -2 * -1 would need to cross it
            ([-2, 3, -4], 24),           # two negatives multiply to a positive; tracking only the max gives 3
            ([-2], -2),                  # single negative, must not return 0 or 1
            ([0, 2], 2),                 # a zero resets the running products
            ([2, -5, -2, -4, 3], 24),    # -2 * -4 * 3, three negatives in a row
            ([-1, -2, -3, 0], 6),        # -2 * -3; the full run -1 * -2 * -3 = -6 is worse
            ([3, -1, 4], 4),             # the negative splits it; 4 alone beats 3
            ([1, 2, 3, 4], 24),          # all positive, the whole array
            ([-3, -1, -1], 3),           # -3 * -1
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.max_product(nums), expected)


if __name__ == '__main__':
    unittest.main()
