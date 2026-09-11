import unittest
from clone_graph import Solution, Node


def build_graph(adj_list):
    # adj_list is LeetCode's format: adj_list[i] lists the 1-indexed neighbors of node i+1.
    if not adj_list:
        return None
    nodes = {i + 1: Node(i + 1) for i in range(len(adj_list))}
    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]
    return nodes[1]


def to_adj_list(node):
    if node is None:
        return []
    visited = {}
    order = []

    def dfs(n):
        if n.val in visited:
            return
        visited[n.val] = True
        order.append(n)
        for nb in n.neighbors:
            dfs(nb)

    dfs(node)
    order.sort(key=lambda n: n.val)
    return [sorted(nb.val for nb in n.neighbors) for n in order]


class TestCloneGraph(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_clone_graph(self):
        cases = [
            [[2, 4], [1, 3], [2, 4], [1, 3]],   # 4-cycle
            [[]],                                 # single isolated node
            [],                                    # empty graph
            [[2], [1]],                            # two nodes, one edge
        ]

        for adj_list in cases:
            with self.subTest(adj_list=adj_list):
                original = build_graph(adj_list)
                clone = self.solution.clone_graph(original)
                self.assertEqual(to_adj_list(clone), adj_list if adj_list != [[]] else [[]])
                if original is not None:
                    self.assertIsNot(clone, original)  # must be a real copy, not the same object


if __name__ == '__main__':
    unittest.main()
