import unittest
from number_of_islands import Solution


def make_grid(rows):
    # Build a fresh list-of-lists grid from strings so each case gets its own copy.
    return [list(row) for row in rows]


class TestNumberOfIslands(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_num_islands(self):
        cases = [
            # (rows, expected)
            (["11000",
              "11000",
              "00100",
              "00011"], 3),
            (["111",
              "010",
              "111"], 1),                    # connected through the middle
            (["0"], 0),                      # single water cell
            (["1"], 1),                      # single land cell
            (["11111"], 1),                  # one row
            (["1", "0", "1", "0", "1"], 3),  # one column
            (["10101",
              "01010",
              "10101"], 8),                  # checkerboard: diagonals do not connect
            (["1111",
              "1001",
              "1001",
              "1111"], 1),                   # ring around water
            (["0000",
              "0000"], 0),                   # all water
            (["1100",
              "1100",
              "0011",
              "0011"], 2),                   # two blocks touching only at a corner
            (["1" * 300] * 300, 1),          # upper bound, one giant island (would overflow naive recursion)
        ]

        for rows, expected in cases:
            with self.subTest(grid=rows):
                result = self.solution.num_islands(make_grid(rows))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
