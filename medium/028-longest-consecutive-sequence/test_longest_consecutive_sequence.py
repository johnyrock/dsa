import unittest
from longest_consecutive_sequence import Solution


class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longest_consecutive(self):
        cases = [
            # (nums, expected)
            ([100, 4, 200, 1, 3, 2], 4),               # the running example in the walkthrough: 1, 2, 3, 4
            ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),       # 0..8, with a duplicate 0 that must not count twice
            ([], 0),                                    # empty input
            ([7], 1),                                   # a single value is a run of length 1
            ([1, 1, 1], 1),                             # duplicates only
            ([-3, -2, -1, 0], 4),                       # negatives and zero
            ([10, 5, 12, 3, 55, 30, 4, 11, 2], 4),      # two runs of 3 (10..12) and 4 (2..5); take the longer
            ([1, 2, 0, 1], 3),                          # 0, 1, 2 with a repeated 1
            ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),   # -1..5, another duplicate
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.longest_consecutive(nums), expected)


if __name__ == '__main__':
    unittest.main()
