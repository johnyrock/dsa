import unittest
from min_cost_climbing_stairs import Solution


class TestMinCostClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_min_cost_climbing_stairs(self):
        cases = [
            ([10, 15, 20], 15),
            ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
            ([0, 0], 0),                     # start from either step for free
            ([1, 2], 1),
        ]
        for cost, expected in cases:
            with self.subTest(cost=cost):
                self.assertEqual(self.solution.min_cost_climbing_stairs(cost), expected)


if __name__ == '__main__':
    unittest.main()
