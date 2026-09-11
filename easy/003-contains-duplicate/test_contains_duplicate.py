import unittest
from contains_duplicate import Solution


class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_contains_duplicate(self):
        cases = [
            # (nums, expected)
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
            ([1], False),                          # single element, nothing to repeat
            ([2, 2], True),                        # shortest possible duplicate
            ([-1, -2, -3, -1], True),              # negatives
            ([0, 4, 3, 0], True),                  # zero counts like any other value
            ([5, -5, 10, -10], False),             # same magnitudes, different signs, all distinct
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                result = self.solution.contains_duplicate(nums)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
