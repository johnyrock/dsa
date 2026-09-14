import unittest
from redundant_connection import Solution


class TestRedundantConnection(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_redundant_connection(self):
        cases = [
            # (edges, expected)
            ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),   # the running example: [1,5] comes later but is not in the cycle
            ([[1, 2], [1, 3], [2, 3]], [2, 3]),                   # triangle, last edge closes it
            ([[1, 2], [2, 3], [1, 3], [3, 4]], [1, 3]),           # extra edge is not the last edge in the input
            ([[1, 2], [2, 3], [3, 1]], [3, 1]),                   # endpoints given with a > b order still returned as given
            ([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]], [2, 5]),   # merges happen out of label order
            ([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]], [1, 3]),   # node 5 only appears in the very last edge; parent must have n + 1 slots
        ]

        for edges, expected in cases:
            with self.subTest(edges=edges):
                result = self.solution.find_redundant_connection(edges)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
