import unittest
from surrounded_regions import Solution


def grid(*rows: str) -> list[list[str]]:
    return [list(row) for row in rows]


class TestSurroundedRegions(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solve(self):
        cases = [
            # (board, expected)
            (grid("XXXXX", "XOOXO", "XXOXO", "XOXXX"),
             grid("XXXXX", "XXXXO", "XXXXO", "XOXXX")),       # the running example: interior blob captured, edge O's kept
            (grid("XXXX", "XOOX", "XXOX", "XOXX"),
             grid("XXXX", "XXXX", "XXXX", "XOXX")),           # LeetCode example 1: bottom-row O survives
            (grid("X"), grid("X")),                          # single cell, nothing to do
            (grid("O"), grid("O")),                          # a lone O is on the border, so it survives
            (grid("OOO", "OXO", "OOO"), grid("OOO", "OXO", "OOO")),   # ring of O's all touch the border
            (grid("XXX", "XOX", "XXX"), grid("XXX", "XXX", "XXX")),   # one fully enclosed O gets captured
            (grid("OXO", "XOX", "OXO"), grid("OXO", "XXX", "OXO")),   # centre O only touches border O's diagonally: captured
            (grid("XOXX", "XOXX", "XOXX", "XXXX"),
             grid("XOXX", "XOXX", "XOXX", "XXXX")),           # a column that reaches the top edge is safe all the way down
            (grid("OOOO", "OOOO", "OOOO"), grid("OOOO", "OOOO", "OOOO")),   # all O: everything connects to the border
        ]

        for board, expected in cases:
            with self.subTest(board=["".join(r) for r in board]):
                self.solution.solve(board)
                self.assertEqual(board, expected)


if __name__ == '__main__':
    unittest.main()
