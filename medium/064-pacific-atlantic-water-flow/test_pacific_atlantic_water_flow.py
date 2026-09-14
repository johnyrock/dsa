import unittest
from pacific_atlantic_water_flow import Solution


class TestPacificAtlanticWaterFlow(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_pacific_atlantic(self):
        cases = [
            # (heights, expected)  -- order does not matter, both sides are sorted before comparing
            ([[1, 2, 2, 3, 5],
              [3, 2, 3, 4, 4],
              [2, 4, 5, 3, 1],
              [6, 7, 1, 4, 5],
              [5, 1, 1, 2, 4]],
             [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]),   # the running example
            ([[1]], [[0, 0]]),                                            # one cell touches both oceans
            ([[1, 1], [1, 1]], [[0, 0], [0, 1], [1, 0], [1, 1]]),         # all equal: every cell reaches both
            ([[1, 2, 3]], [[0, 0], [0, 1], [0, 2]]),                      # one row: every cell is on both edges
            ([[3], [2], [1]], [[0, 0], [1, 0], [2, 0]]),                  # one column, same reason
            ([[1, 2, 3],
              [8, 9, 4],
              [7, 6, 5]],
             [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]),   # a spiral; (0, 0) and (0, 1) cannot climb to reach the Atlantic
            ([[10, 10, 10],
              [10, 1, 10],
              [10, 10, 10]],
             [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]),  # a pit in the middle reaches nothing
            ([[1, 2, 1],
              [2, 3, 2],
              [1, 2, 1]],
             [[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1]]),   # a peak in the middle drains everywhere except the two corner pits
            ([[5, 1],
              [1, 5]],
             [[0, 0], [0, 1], [1, 0], [1, 1]]),                           # both diagonals are on both edges anyway
            ([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]],
             [[0, 2], [1, 2], [2, 0], [2, 1], [2, 2]]),                   # strictly increasing: only the Atlantic edge cells also reach the Pacific
        ]

        for heights, expected in cases:
            with self.subTest(heights=heights):
                result = self.solution.pacific_atlantic([row[:] for row in heights])
                self.assertEqual(sorted(result), sorted(expected))

    def test_upper_bound_all_equal(self):
        n = 200
        heights = [[7] * n for _ in range(n)]
        result = self.solution.pacific_atlantic(heights)
        self.assertEqual(len(result), n * n)


if __name__ == '__main__':
    unittest.main()
