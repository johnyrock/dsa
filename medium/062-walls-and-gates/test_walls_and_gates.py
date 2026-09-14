import unittest
from walls_and_gates import Solution

INF = 2147483647


class TestWallsAndGates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_walls_and_gates(self):
        cases = [
            # (rooms, expected)
            ([[INF, -1, 0, INF],
              [INF, INF, INF, -1],
              [INF, -1, INF, -1],
              [0, -1, INF, INF]],
             [[3, -1, 0, 1],
              [2, 2, 1, -1],
              [1, -1, 2, -1],
              [0, -1, 3, 4]]),                       # the running example
            ([[-1]], [[-1]]),                         # a single wall
            ([[0]], [[0]]),                           # a single gate
            ([[INF]], [[INF]]),                       # a single room with no gate stays INF
            ([[INF, -1, 0]], [[INF, -1, 0]]),         # wall cuts the room off
            ([[0, INF, INF, INF]], [[0, 1, 2, 3]]),   # one row, one gate
            ([[0, INF, INF, 0]], [[0, 1, 1, 0]]),     # two gates: middle rooms take the nearer one
            ([[INF, INF], [INF, INF]],
             [[INF, INF], [INF, INF]]),               # no gates at all
            ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),     # all gates: nothing to fill
            ([[INF, 0], [INF, -1], [INF, INF]],
             [[1, 0], [2, -1], [3, 4]]),              # the path must wind around the wall
            ([[0, INF, INF],
              [INF, INF, INF],
              [INF, INF, 0]],
             [[0, 1, 2],
              [1, 2, 1],
              [2, 1, 0]]),                            # one-gate-at-a-time BFS would give 3 at (1, 2) and (2, 1)
            ([], []),                                 # empty grid
        ]

        for rooms, expected in cases:
            with self.subTest(rooms=rooms):
                grid = [row[:] for row in rooms]
                self.assertIsNone(self.solution.walls_and_gates(grid))
                self.assertEqual(grid, expected)

    def test_large_grid_stays_fast(self):
        n = 250
        grid = [[INF] * n for _ in range(n)]
        grid[0][0] = 0
        self.solution.walls_and_gates(grid)
        self.assertEqual(grid[n - 1][n - 1], 2 * (n - 1))
        self.assertEqual(grid[0][n - 1], n - 1)


if __name__ == '__main__':
    unittest.main()
