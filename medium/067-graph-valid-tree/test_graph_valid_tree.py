import unittest
from graph_valid_tree import Solution


class TestGraphValidTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_tree(self):
        cases = [
            # (n, edges, expected)
            (5, [[0, 1], [0, 2], [0, 3], [1, 4]], True),              # the running example: a star with one extra leaf
            (5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], False),     # 1-2-3 forms a cycle
            (5, [[0, 1], [1, 2], [3, 4]], False),                     # no cycle but two components: a forest, not a tree
            (1, [], True),                                            # a single node is a tree
            (2, [], False),                                           # two nodes, no edge: disconnected
            (2, [[0, 1]], True),
            (3, [[0, 1], [1, 2], [0, 2]], False),                     # triangle: 3 edges on 3 nodes
            (4, [[0, 1], [2, 3], [1, 2]], True),                      # a path given in a scrambled edge order
            (4, [[0, 1], [0, 2], [0, 3], [1, 2]], False),             # right count of edges? no: 4 edges on 4 nodes
            (6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]], True),      # a long chain, exercises path halving
        ]

        for n, edges, expected in cases:
            with self.subTest(n=n, edges=edges):
                result = self.solution.valid_tree(n, edges)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
