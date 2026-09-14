import unittest
from balanced_binary_tree import Solution, TreeNode


def build_tree(values):
    # Level-order build with None gaps, the format LeetCode uses in examples.
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


def tree_to_list(root):
    # Level-order dump, trimmed of trailing Nones so equality checks read cleanly.
    if root is None:
        return []
    values = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            values.append(None)
            continue
        values.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while values and values[-1] is None:
        values.pop()
    return values


class TestBalancedBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_balanced_binary_tree(self):
        cases = [
            ([3, 9, 20, None, None, 15, 7], True),
            ([1, 2, 2, 3, 3, None, None, 4, 4], False),
            ([], True),                         # an empty tree is balanced
            ([1], True),
            ([1, 2, 3, 4, None, None, None, 5], False),
        ]
        for values, expected in cases:
            with self.subTest(values=values):
                self.assertEqual(self.solution.is_balanced(build_tree(values)), expected)


if __name__ == '__main__':
    unittest.main()
