import unittest
from spiral_matrix import Solution


class TestSpiralMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_spiral_order(self):
        cases = [
            # (matrix, expected)
            ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),  # the running example
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),   # odd square: single centre cell
            ([[1]], [1]),                                                         # 1 x 1
            ([[1, 2, 3]], [1, 2, 3]),                                             # single row: bottom walk must be skipped
            ([[1], [2], [3]], [1, 2, 3]),                                         # single column: left walk must be skipped
            ([[1, 2], [3, 4]], [1, 2, 4, 3]),
            ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 6, 5, 4]),                         # 2 x 3: second layer is empty
            ([[1, 2], [3, 4], [5, 6]], [1, 2, 4, 6, 5, 3]),                       # 3 x 2: inner layer is one cell wide
        ]
        for matrix, expected in cases:
            with self.subTest(matrix=matrix):
                self.assertEqual(self.solution.spiral_order(matrix), expected)


if __name__ == '__main__':
    unittest.main()
