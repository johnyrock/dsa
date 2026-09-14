import unittest
from rotate_image import Solution


class TestRotateImage(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rotate(self):
        cases = [
            # (matrix, expected after one clockwise rotation)
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),   # the running example
            ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
             [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
            ([[1]], [[1]]),                                                         # 1 x 1, nothing to swap
            ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),                                   # single swap then two reversals
            ([[-1, 0], [0, -1]], [[0, -1], [-1, 0]]),                               # negative values are just values
        ]
        for matrix, expected in cases:
            with self.subTest(matrix=matrix):
                copy = [row[:] for row in matrix]
                self.solution.rotate(copy)
                self.assertEqual(copy, expected)

    def test_four_rotations_restore(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        copy = [row[:] for row in matrix]
        for _ in range(4):
            self.solution.rotate(copy)
        self.assertEqual(copy, matrix)


if __name__ == '__main__':
    unittest.main()
