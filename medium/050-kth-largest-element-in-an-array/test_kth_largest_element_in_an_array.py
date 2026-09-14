import unittest
from kth_largest_element_in_an_array import Solution


class TestKthLargestElementInAnArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_kth_largest(self):
        cases = [
            # (nums, k, expected)
            ([3, 2, 1, 5, 6, 4], 2, 5),                 # the running example in the walkthrough
            ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),        # duplicates count separately: 6, 5, 5, 4
            ([1], 1, 1),                                # single element
            ([3, 2, 1, 5, 6, 4], 1, 6),                 # k = 1 is the maximum
            ([3, 2, 1, 5, 6, 4], 6, 1),                 # k = len is the minimum, nothing ever popped
            ([2, 2, 2, 2], 3, 2),                       # all equal
            ([-1, -5, -3, -2], 2, -2),                  # negatives
            ([5, 4, 3, 2, 1], 3, 3),                    # descending input, every early push gets evicted later
            ([1, 2, 3, 4, 5], 3, 3),                    # ascending input, every push evicts the previous root
            ([10000, -10000, 0], 2, 0),                 # constraint extremes
        ]

        for nums, k, expected in cases:
            with self.subTest(nums=nums, k=k):
                result = self.solution.find_kth_largest(nums, k)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
