import unittest
from validate_binary_search_tree import Solution, TreeNode


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


class TestValidateBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_valid_bst(self):
        cases = [
            # (level-order input, expected)
            ([2, 1, 3], True),
            ([5, 1, 4, None, None, 3, 6], False),   # 3 is a right-grandchild < root 5's ancestor 4 is fine, but 3 < 4's left bound
            ([1], True),
            ([], True),
            ([5, 4, 6, None, None, 3, 7], False),   # 3 violates the inherited lower bound from root 5
            ([2, 2, 2], False),                     # equal values are not strictly less/greater
        ]

        for values, expected in cases:
            with self.subTest(values=values):
                result = self.solution.is_valid_bst(build_tree(values))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
