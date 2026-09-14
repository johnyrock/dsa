import unittest
from partition_equal_subset_sum import Solution


class TestPartitionEqualSubsetSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_can_partition(self):
        cases = [
            # (nums, expected)
            ([1, 5, 11, 5], True),          # the running example: {1, 5, 5} and {11}
            ([1, 2, 3, 5], False),          # total 11 is odd
            ([1, 2, 5], False),             # total 8 is even, but no subset sums to 4; ascending loop would say True
            ([1], False),                   # a single element cannot be split
            ([2, 2], True),                 # smallest even split
            ([1, 1], True),
            ([3, 3, 3, 4, 5], True),        # {3, 3, 3} = 9 and {4, 5} = 9
            ([1, 2, 3, 4, 5, 6, 7], True),  # total 28, target 14
            ([100, 100], True),             # maximum element value
            ([2, 4, 8], False),             # even total 14 but 7 is unreachable
            ([14, 9, 8, 4, 3, 2], True),    # {14, 6} vs {9, 8, 3}: 20 = 20
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                result = self.solution.can_partition(list(nums))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
