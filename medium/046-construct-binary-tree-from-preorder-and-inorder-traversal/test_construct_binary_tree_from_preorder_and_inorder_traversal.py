import unittest
from construct_binary_tree_from_preorder_and_inorder_traversal import Solution


def tree_to_list(root):
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


class TestConstructBinaryTreeFromPreorderAndInorderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_build_tree(self):
        cases = [
            # (preorder, inorder, expected level order)
            ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),   # the running example
            ([-1], [-1], [-1]),                                                       # single node
            ([1, 2, 3], [3, 2, 1], [1, 2, None, 3]),                                  # left-skewed chain: inorder is reversed preorder
            ([1, 2, 3], [1, 2, 3], [1, None, 2, None, 3]),                            # right-skewed chain: inorder equals preorder
            ([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7], [1, 2, 3, 4, 5, 6, 7]),    # full tree
            ([1, 2, 3], [2, 1, 3], [1, 2, 3]),                                        # root with two leaves
            ([2, 1, 3], [1, 2, 3], [2, 1, 3]),                                        # same inorder as above, different preorder
            ([1, 2, 3, 4], [2, 3, 1, 4], [1, 2, 4, None, 3]),                         # left subtree has its own right child
        ]

        for preorder, inorder, expected in cases:
            with self.subTest(preorder=preorder, inorder=inorder):
                result = self.solution.build_tree(list(preorder), list(inorder))
                self.assertEqual(tree_to_list(result), expected)


if __name__ == '__main__':
    unittest.main()
