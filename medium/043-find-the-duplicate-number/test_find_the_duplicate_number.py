import unittest
from find_the_duplicate_number import Solution


class TestFindTheDuplicateNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_duplicate(self):
        cases = [
            # (nums, expected)
            ([1, 3, 4, 2, 2], 2),           # the running example in the walkthrough
            ([3, 1, 3, 4, 2], 3),
            ([3, 3, 3, 3, 3], 3),           # duplicate repeated many times: self-loop at 3
            ([1, 1], 1),                    # smallest input, n = 1
            ([2, 2, 2, 2, 2], 2),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 5], 5),  # cycle entered late: 0 -> 1 -> ... -> 9 -> 5
            ([2, 5, 9, 6, 9, 3, 8, 9, 7, 1], 9),  # a pre-check `while slow != fast` would return 0 here
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                snapshot = list(nums)
                result = self.solution.find_duplicate(nums)
                self.assertEqual(result, expected)
                self.assertEqual(nums, snapshot)  # the array must not be modified


if __name__ == '__main__':
    unittest.main()
