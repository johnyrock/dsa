import unittest
from slug import Solution


class TestSlug(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solve(self):
        cases = [
            # (nums, expected)
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                result = self.solution.solve(nums)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
