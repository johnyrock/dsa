import unittest
from rotting_oranges import Solution


def make_grid(rows):
    # Build a fresh list-of-lists grid from strings so each case gets its own copy (the solution rots cells in place).
    return [[int(ch) for ch in row] for row in rows]


class TestRottingOranges(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_oranges_rotting(self):
        cases = [
            # (rows, expected)
            (["211",
              "110",
              "011"], 4),                  # the running example; `while queue` alone would give 5
            (["211",
              "011",
              "101"], -1),                 # (2, 0) is cut off by empty cells
            (["02"], 0),                   # no fresh oranges, no time passes
            (["0"], 0),                    # single empty cell
            (["1"], -1),                   # single fresh orange and nothing to rot it
            (["2"], 0),                    # single rotten orange
            (["21"], 1),                   # one step
            (["2111"], 3),                 # a line: one orange per minute
            (["1112"], 3),                 # rot spreads leftward just as well
            (["2112"], 1),                 # two sources meet in the middle
            (["211",
              "111",
              "112"], 2),                  # two sources from opposite corners; one source would take 4
            (["2000",
              "1000",
              "1000",
              "1001"], -1),                # a reachable column and one unreachable orange
            (["1111",
              "1001",
              "1001",
              "1112"], 6),                 # rot goes both ways around the ring
            (["2222",
              "2222"], 0),                 # all rotten already
            (["0000",
              "0000"], 0),                 # nothing at all
            (["1010",
              "0101"], -1),                # fresh oranges only touch diagonally, nothing rotten
        ]

        for rows, expected in cases:
            with self.subTest(grid=rows):
                result = self.solution.oranges_rotting(make_grid(rows))
                self.assertEqual(result, expected)

    def test_upper_bound(self):
        grid = [[1] * 10 for _ in range(10)]
        grid[0][0] = 2
        self.assertEqual(self.solution.oranges_rotting(grid), 18)


if __name__ == '__main__':
    unittest.main()
