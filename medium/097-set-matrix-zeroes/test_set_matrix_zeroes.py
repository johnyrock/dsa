import unittest
from set_matrix_zeroes import Solution


class TestSetMatrixZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_set_zeroes(self):
        cases = [
            # (matrix, expected)
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),                     # the running example: one interior zero
            ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),   # zeros in row 0 and column 0 themselves
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),                     # no zeros: untouched
            ([[0]], [[0]]),                                                                             # 1 x 1
            ([[1, 0]], [[0, 0]]),                                                                       # single row, zero in row 0
            ([[1], [0]], [[0], [0]]),                                                                   # single column, zero in column 0
            ([[1, 2], [0, 4]], [[0, 2], [0, 0]]),                                                       # zero in column 0 only: row 1 and column 0 cleared, row 0 keeps its 2
            ([[0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0]]),                                           # all zeros
            ([[1, 2, 3], [4, 0, 6], [7, 8, 0]], [[1, 0, 0], [0, 0, 0], [0, 0, 0]]),                     # two zeros sharing a row/column with markers
        ]
        for matrix, expected in cases:
            with self.subTest(matrix=matrix):
                copy = [row[:] for row in matrix]
                self.solution.set_zeroes(copy)
                self.assertEqual(copy, expected)


if __name__ == '__main__':
    unittest.main()
