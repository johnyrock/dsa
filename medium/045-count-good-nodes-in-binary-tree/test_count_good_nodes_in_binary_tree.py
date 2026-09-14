import unittest
from count_good_nodes_in_binary_tree import Solution, TreeNode


def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class TestCountGoodNodesInBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_good_nodes(self):
        cases = [
            # (level-order input, expected)
            ([3, 1, 4, 3, None, 1, 5], 4),        # the running example: 3, 4, 3, 5
            ([3, 3, None, 4, 2], 3),              # equal value is still good; 2 is blocked by 3 and 4
            ([1], 1),                             # the root is always good
            ([9, 8, 7, 6, 5, 4, 3], 1),           # strictly decreasing: only the root
            ([1, 2, 3, 4, 5, 6, 7], 7),           # every child exceeds its ancestors
            ([-1, -2, -3], 1),                    # negative values: -inf seed still makes the root good
            ([2, None, 2, None, 2], 3),           # a chain of equal values is all good
            ([5, 3, 7, 2, 4, 6, 8], 3),           # 5, 7, 8
            ([1, 10, 2], 3),                      # a shared (non-path) maximum would wrongly block the 2
        ]

        for values, expected in cases:
            with self.subTest(values=values):
                result = self.solution.good_nodes(build_tree(values))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
