import unittest
from binary_tree_level_order_traversal import Solution, TreeNode


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


class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_level_order(self):
        cases = [
            # (level-order input, expected levels)
            ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
            ([1], [[1]]),
            ([], []),
            ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),  # complete tree
            ([1, None, 2, None, 3], [[1], [2], [3]]),               # right-skewed chain
        ]

        for values, expected in cases:
            with self.subTest(values=values):
                result = self.solution.level_order(build_tree(values))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
