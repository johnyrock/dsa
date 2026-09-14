import unittest
from min_cost_to_connect_all_points import Solution


class TestMinCostToConnectAllPoints(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_min_cost_connect_points(self):
        cases = [
            # (points, expected)
            ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),      # the running example: 4 + 3 + 4 + 9
            ([[3, 12], [-2, 5], [-4, 1]], 18),                     # three points, skip the longest side
            ([[0, 0], [1, 1], [1, 0], [-1, 1]], 4),                # 1 + 1 + 2
            ([[0, 0]], 0),                                         # a single point costs nothing
            ([[0, 0], [1, 0]], 1),                                 # two points, one edge
            ([[-1000000, -1000000], [1000000, 1000000]], 4000000), # extreme coordinates, Manhattan not Euclidean
            ([[0, 0], [3, 4]], 7),                                 # Manhattan 7; Euclidean would give 5
            ([[2, -3], [-17, -8], [13, 8], [-17, -15]], 53),       # negatives; stale heap entries must be skipped
        ]

        for points, expected in cases:
            with self.subTest(points=points):
                result = self.solution.min_cost_connect_points(points)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
