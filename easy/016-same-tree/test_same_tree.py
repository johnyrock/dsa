import unittest
from same_tree import Solution, TreeNode


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


class TestSameTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_same_tree(self):
        cases = [
            ([1, 2, 3], [1, 2, 3], True),
            ([1, 2], [1, None, 2], False),
            ([1, 2, 1], [1, 1, 2], False),
            ([], [], True),                    # two empty trees match
            ([], [1], False),
        ]
        for left, right, expected in cases:
            with self.subTest(left=left, right=right):
                self.assertEqual(self.solution.is_same_tree(build_tree(left), build_tree(right)), expected)


if __name__ == '__main__':
    unittest.main()
