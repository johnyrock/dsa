import unittest
from valid_sudoku import Solution


def make_board(rows):
    return [list(row) for row in rows]


VALID = [
    "53..7....",
    "6..195...",
    ".98....6.",
    "8...6...3",
    "4..8.3..1",
    "7...2...6",
    ".6....28.",
    "...419..5",
    "....8..79",
]


class TestValidSudoku(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_valid_sudoku(self):
        empty = ["........."] * 9
        box_dup = VALID[:]
        box_dup[0] = "83..7...."          # 8 at (0,0) repeats the 8 at (2,2): same box, different row and column
        row_dup = VALID[:]
        row_dup[0] = "53..7...5"          # second 5 in row 0, far from the first box
        col_dup = VALID[:]
        col_dup[8] = "5...8..79"          # 5 at (8,0) repeats the 5 at (0,0) in column 0
        diag_ok = VALID[:]
        diag_ok[8] = "....8.679"          # 6 at (8,6) shares no row, column, or box with the other 6s
        cross_box = empty[:]
        cross_box[0] = "......1.."        # 1 at (0,6), box 2
        cross_box[3] = "...1....."        # 1 at (3,3), box 4: different row, column, and box, so valid

        cases = [
            # (rows, expected)
            (VALID, True),                # the running example in the walkthrough
            (box_dup, False),             # LeetCode example 2
            (row_dup, False),
            (col_dup, False),
            (diag_ok, True),
            (empty, True),                # no digits means no violations
            (cross_box, True),            # r // 3 + c // 3 would wrongly merge these boxes
        ]

        for rows, expected in cases:
            with self.subTest(rows=rows):
                self.assertEqual(self.solution.is_valid_sudoku(make_board(rows)), expected)


if __name__ == '__main__':
    unittest.main()
