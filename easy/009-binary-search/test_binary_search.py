import unittest
from binary_search import Solution


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_search(self):
        cases = [
            # (nums, target, expected)
            ([-1, 0, 3, 5, 9, 12], 9, 4),
            ([-1, 0, 3, 5, 9, 12], 2, -1),      # absent, lo crosses hi
            ([1, 2, 3, 4, 5], 5, 4),            # last element, the case `while lo < hi` misses
            ([1, 2, 3, 4, 5], 1, 0),            # first element
            ([5], 5, 0),                        # single element, found
            ([5], -5, -1),                      # single element, absent
            ([], 1, -1),                        # empty array, loop body never runs
            ([2, 4, 6, 8], 5, -1),              # even length, target falls between two values
        ]

        for nums, target, expected in cases:
            with self.subTest(nums=nums, target=target):
                result = self.solution.search(nums, target)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
