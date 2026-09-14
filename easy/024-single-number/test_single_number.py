import unittest
from single_number import Solution


class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_number(self):
        cases = [
            ([2, 2, 1], 1),
            ([4, 1, 2, 1, 2], 4),
            ([1], 1),                          # one value has no pair
            ([-1, -1, -2], -2),
        ]
        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.single_number(nums), expected)


if __name__ == '__main__':
    unittest.main()
