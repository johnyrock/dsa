import unittest
from max_area_of_island import Solution


def make_grid(rows):
    # Build a fresh list-of-lists grid from strings so each case gets its own copy (the solution sinks cells in place).
    return [[int(ch) for ch in row] for row in rows]


class TestMaxAreaOfIsland(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_area_of_island(self):
        cases = [
            # (rows, expected)
            (["00100",
              "01100",
              "00010",
              "10111"], 4),                  # the running example: areas 3, 4, 1
            (["00000000"], 0),               # no land at all
            (["110",
              "110",
              "001"], 4),                    # corner cell touches the block only diagonally
            (["1"], 1),                      # single land cell
            (["0"], 0),                      # single water cell
            (["11111"], 5),                  # one row
            (["1", "1", "0", "1"], 2),       # one column, two islands
            (["10101",
              "01010",
              "10101"], 1),                  # checkerboard: every cell is its own island
            (["1111",
              "1001",
              "1001",
              "1111"], 12),                  # ring around water
            (["0000000010",
              "0000000011",
              "0000000000",
              "1100000000",
              "1110000000"], 5),             # the larger island is found after a smaller one
            (["11000",
              "11000",
              "00111",
              "00111"], 6),                  # two blocks touching only at a corner; not-resetting area would give 10
            (["1" * 50] * 50, 2500),         # upper bound, one giant island
        ]

        for rows, expected in cases:
            with self.subTest(grid=rows):
                result = self.solution.max_area_of_island(make_grid(rows))
                self.assertEqual(result, expected)

    def test_leetcode_example(self):
        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
        self.assertEqual(self.solution.max_area_of_island(grid), 6)


if __name__ == '__main__':
    unittest.main()
