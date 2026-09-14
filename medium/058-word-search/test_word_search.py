import unittest
from word_search import Solution


class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_exist(self):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        cases = [
            # (word, expected)
            ("ABCCED", True),    # the running example, a six-cell path with a turn
            ("SEE", True),       # must skip the S at (1,0) and start from (1,3)
            ("ABCB", False),     # would need to reuse the single B
            ("A", True),         # single letter, no neighbours needed
            ("CCB", True),       # fails from (0,2) first; only found if that attempt unmarks its cells
            ("ABCESEEDASF", True),  # eleven-cell snake around the whole board
            ("Z", False),        # letter not on the board
        ]

        for word, expected in cases:
            with self.subTest(word=word):
                snapshot = [row[:] for row in board]
                result = self.solution.exist(board, word)
                self.assertEqual(result, expected)
                self.assertEqual(board, snapshot)   # every mark must be undone

    def test_single_cell_board(self):
        self.assertTrue(self.solution.exist([["a"]], "a"))
        self.assertFalse(self.solution.exist([["a"]], "aa"))   # cannot reuse the one cell


if __name__ == '__main__':
    unittest.main()
