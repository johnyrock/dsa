import unittest
from binary_tree_right_side_view import Solution, TreeNode


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


class TestBinaryTreeRightSideView(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_right_side_view(self):
        cases = [
            # (level-order input, expected)
            ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),          # the running example in the walkthrough
            ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]), # deep nodes live in the LEFT subtree
            ([1, None, 3], [1, 3]),
            ([1, 2], [1, 2]),                                   # a lone left child is visible from the right
            ([], []),
            ([1], [1]),
            ([1, 2, 3, 4, 5, 6, 7], [1, 3, 7]),                 # complete tree: the right spine
            ([1, 2, None, 3, None, 4], [1, 2, 3, 4]),           # left-skewed chain
        ]

        for values, expected in cases:
            with self.subTest(values=values):
                result = self.solution.right_side_view(build_tree(values))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
