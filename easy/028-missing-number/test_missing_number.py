import unittest
from missing_number import Solution


class TestMissingNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_missing_number(self):
        cases = [
            ([3, 0, 1], 2),
            ([0, 1], 2),
            ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
            ([1], 0),                          # the missing value can be zero
            ([], 0),
        ]
        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.missing_number(nums), expected)


if __name__ == '__main__':
    unittest.main()
