import unittest
from longest_increasing_subsequence import Solution


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_length_of_lis(self):
        cases = [
            # (nums, expected)
            ([10, 9, 2, 5, 3, 7, 101, 18], 4),   # the running example: 2, 3, 7, 101 (or 2, 5, 7, 18)
            ([0, 1, 0, 3, 2, 3], 4),             # 0, 1, 2, 3
            ([7, 7, 7, 7, 7, 7, 7], 1),          # strictly increasing: equal values never chain; <= would give 7
            ([1], 1),                            # single element
            ([5, 4, 3, 2, 1], 1),                # strictly decreasing
            ([1, 2, 3, 4, 5], 5),                # already sorted
            ([4, 5, 1], 2),                      # the LIS does not end at the last index; dp[-1] would give 1
            ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),   # 1, 3, 6, 7, 9, 10
            ([-2, -1], 2),                       # negatives allowed
            ([2, 2, 1], 1),
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                result = self.solution.length_of_lis(list(nums))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
