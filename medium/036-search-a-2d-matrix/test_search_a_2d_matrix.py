import unittest
from search_a_2d_matrix import Solution


class TestSearchA2dMatrix(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_search_matrix(self):
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        cases = [
            # (matrix, target, expected)
            (matrix, 3, True),                       # the running example in the walkthrough
            (matrix, 13, False),                     # falls between rows 1 and 2
            (matrix, 1, True),                       # first element; `while lo < hi` still finds it via mid = 0
            (matrix, 60, True),                      # last element; `while lo < hi` misses it
            (matrix, 0, False),                      # below everything
            (matrix, 61, False),                     # above everything
            (matrix, 23, True),                      # first element of a row: mid // cols must use cols, not rows
            ([[1]], 1, True),                        # 1 x 1
            ([[1]], 2, False),
            ([[1, 3]], 3, True),                     # single row
            ([[1], [3]], 3, True),                   # single column
            ([[1, 2, 3, 4, 5, 6]], 4, True),         # 1 x 6: mid // rows would index out of range
        ]

        for m, target, expected in cases:
            with self.subTest(target=target, shape=(len(m), len(m[0]))):
                result = self.solution.search_matrix(m, target)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
