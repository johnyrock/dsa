import unittest
from subtree_of_another_tree import Solution, TreeNode


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


class TestSubtreeOfAnotherTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_subtree_of_another_tree(self):
        cases = [
            ([3, 4, 5, 1, 2], [4, 1, 2], True),
            ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
            ([1], [1], True),
            ([1, 1], [1], True),               # either matching node can be the root
            ([1, 2], [1, 2, 3], False),
        ]
        for values, candidate, expected in cases:
            with self.subTest(values=values, candidate=candidate):
                self.assertEqual(self.solution.is_subtree(build_tree(values), build_tree(candidate)), expected)


if __name__ == '__main__':
    unittest.main()
