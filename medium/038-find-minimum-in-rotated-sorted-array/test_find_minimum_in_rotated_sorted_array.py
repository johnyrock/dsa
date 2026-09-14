import unittest
from find_minimum_in_rotated_sorted_array import Solution


class TestFindMinimumInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_min(self):
        cases = [
            # (nums, expected)
            ([4, 5, 6, 7, 0, 1, 2], 0),   # the running example in the walkthrough
            ([3, 4, 5, 1, 2], 1),
            ([11, 13, 15, 17], 11),       # not rotated at all: the first element is the answer
            ([1], 1),                     # single element, loop never runs
            ([2, 1], 1),                  # two elements, rotated once
            ([1, 2], 1),                  # two elements, not rotated
            ([3, 1, 2], 1),               # minimum in the middle; hi = mid - 1 here would return 3
            ([2, 3, 4, 5, 1], 1),         # rotated so the minimum is last
            ([5, 1, 2, 3, 4], 1),         # rotated so the minimum is second
            ([-5, -3, -1, -7, -6], -7),   # negatives, same logic
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                result = self.solution.find_min(nums)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
