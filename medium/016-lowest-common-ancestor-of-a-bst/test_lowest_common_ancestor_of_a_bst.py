import unittest
from lowest_common_ancestor_of_a_bst import Solution, TreeNode


class TestLowestCommonAncestorOfABst(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        # Standard example tree:
        #              6
        #           /     \
        #          2        8
        #        /   \    /   \
        #       0     4  7     9
        #            / \
        #           3   5
        self.n0 = TreeNode(0)
        self.n3 = TreeNode(3)
        self.n5 = TreeNode(5)
        self.n4 = TreeNode(4, self.n3, self.n5)
        self.n2 = TreeNode(2, self.n0, self.n4)
        self.n7 = TreeNode(7)
        self.n9 = TreeNode(9)
        self.n8 = TreeNode(8, self.n7, self.n9)
        self.root = TreeNode(6, self.n2, self.n8)

    def test_lowest_common_ancestor(self):
        cases = [
            # (p, q, expected value)
            (self.n2, self.n8, 6),   # split at the root
            (self.n2, self.n4, 2),   # one is an ancestor of the other
            (self.n3, self.n5, 4),   # both under the same subtree
            (self.n0, self.n5, 2),   # deeper split
            (self.root, self.n9, 6), # p is the root itself
        ]

        for p, q, expected in cases:
            with self.subTest(p=p.val, q=q.val):
                result = self.solution.lowest_common_ancestor(self.root, p, q)
                self.assertEqual(result.val, expected)


if __name__ == '__main__':
    unittest.main()
