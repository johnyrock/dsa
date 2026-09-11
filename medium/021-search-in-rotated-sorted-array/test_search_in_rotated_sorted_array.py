import unittest
from search_in_rotated_sorted_array import Solution


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_search(self):
        cases = [
            # (nums, target, expected index)
            ([4, 5, 6, 7, 0, 1, 2], 0, 4),
            ([4, 5, 6, 7, 0, 1, 2], 3, -1),
            ([1], 0, -1),
            ([1], 1, 0),
            ([], 5, -1),
            ([5, 1, 3], 5, 0),               # target is the pivot itself
            ([3, 1], 1, 1),                   # tiny rotated array
            (list(range(10)), 7, 7),          # no rotation at all
        ]

        for nums, target, expected in cases:
            with self.subTest(nums=nums, target=target):
                result = self.solution.search(nums, target)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
