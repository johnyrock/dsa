import unittest
from maximum_subarray import Solution


class TestMaximumSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_sub_array(self):
        cases = [
            # (nums, expected)
            ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
            ([1], 1),                            # single element
            ([5, 4, -1, 7, 8], 23),              # whole array
            ([-3, -1, -2], -1),                  # all negative, pick the largest single element
            ([-1], -1),                          # single negative element
            ([0, 0, 0], 0),                      # all zeros
            ([2, -1, 2, -1, 2], 4),              # small dips are worth absorbing
            ([-2, -1], -1),
            ([1, -2, 3, -2, 5], 6),              # 3 + (-2) + 5 beats 5 alone
            ([8, -19, 5, -4, 20], 21),           # restart after a big negative, then absorb a small one
            ([-10000, 10000, -10000, 10000], 10000),
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                result = self.solution.max_sub_array(list(nums))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
