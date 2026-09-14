import unittest
from house_robber import Solution


class TestHouseRobber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rob(self):
        cases = [
            # (nums, expected)
            ([2, 7, 9, 3, 1], 12),        # the running example: 2 + 9 + 1
            ([1, 2, 3, 1], 4),            # 1 + 3, not 2 + 1
            ([2, 1, 1, 2], 4),            # skipping two houses in a row is allowed
            ([5], 5),                     # single house
            ([3, 10], 10),                # two houses, take the larger
            ([0, 0, 0], 0),               # nothing worth taking
            ([4, 1, 1, 4, 1], 8),         # forced alternation (0, 2, 4) gives only 6
            ([1, 3, 1, 3, 100], 103),     # the big house at the end must be reachable
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                result = self.solution.rob(nums)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
