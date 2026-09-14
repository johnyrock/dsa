import unittest
from diameter_of_binary_tree import Solution, TreeNode


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


class TestDiameterOfBinaryTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_diameter_of_binary_tree(self):
        cases = [
            ([1, 2, 3, 4, 5], 3),
            ([1, 2], 1),
            ([1], 0),                        # no edge in a one-node tree
            ([1, 2, None, 3, None, 4], 3),  # a chain counts edges
            ([], 0),
        ]
        for values, expected in cases:
            with self.subTest(values=values):
                self.assertEqual(self.solution.diameter_of_binary_tree(build_tree(values)), expected)


if __name__ == '__main__':
    unittest.main()
