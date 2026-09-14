import unittest
from k_closest_points_to_origin import Solution


class TestKClosestPointsToOrigin(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_k_closest(self):
        cases = [
            # (points, k, expected as a set of tuples, since any order is allowed)
            ([[3, 3], [5, -1], [-2, 4]], 2, {(3, 3), (-2, 4)}),      # the running example in the walkthrough
            ([[1, 3], [-2, 2]], 1, {(-2, 2)}),                        # 8 < 10
            ([[0, 1], [1, 0]], 2, {(0, 1), (1, 0)}),                  # k == len(points), everything survives
            ([[7, 7]], 1, {(7, 7)}),                                  # single point
            ([[0, 0], [10000, 10000], [-10000, -10000]], 1, {(0, 0)}),  # the origin itself, extreme coordinates
            ([[1, 1], [-1, -1], [2, 2], [-2, -2]], 2, {(1, 1), (-1, -1)}),  # negatives square to the same distance
            ([[2, 0], [0, 2], [1, 1], [3, 0]], 3, {(2, 0), (0, 2), (1, 1)}),  # ties at distance 4 both kept
            ([[5, 5], [1, 1], [4, 4], [2, 2], [3, 3]], 3, {(1, 1), (2, 2), (3, 3)}),  # decreasing then increasing
        ]

        for points, k, expected in cases:
            with self.subTest(points=points, k=k):
                result = self.solution.k_closest(points, k)
                self.assertEqual(len(result), k)
                self.assertEqual({tuple(p) for p in result}, expected)


if __name__ == '__main__':
    unittest.main()
