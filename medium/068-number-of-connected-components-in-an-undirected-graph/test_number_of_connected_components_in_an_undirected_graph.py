import unittest
from number_of_connected_components_in_an_undirected_graph import Solution


class TestNumberOfConnectedComponentsInAnUndirectedGraph(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_count_components(self):
        cases = [
            # (n, edges, expected)
            (5, [[0, 1], [1, 2], [3, 4]], 2),                     # the running example: {0,1,2} and {3,4}
            (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),             # one chain through every node
            (1, [], 1),                                           # a single node is one component
            (4, [], 4),                                           # no edges: every node is its own component
            (5, [[0, 1], [1, 2], [3, 4], [0, 2]], 2),             # [0,2] is redundant; must not decrement the count
            (4, [[0, 1], [2, 3], [1, 3]], 1),                     # two pairs joined by a third edge: parent is not flat
            (3, [[0, 1], [1, 2], [0, 2]], 1),                     # a triangle is still one component
            (6, [[0, 1], [2, 3], [4, 5]], 3),                     # three disjoint pairs
            (7, [[0, 1], [1, 2], [2, 0], [3, 4], [5, 6], [4, 5]], 2),   # triangle + a 4-node chain built out of order
        ]

        for n, edges, expected in cases:
            with self.subTest(n=n, edges=edges):
                result = self.solution.count_components(n, edges)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
