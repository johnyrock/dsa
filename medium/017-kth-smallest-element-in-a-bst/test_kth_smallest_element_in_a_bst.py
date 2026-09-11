import unittest
from kth_smallest_element_in_a_bst import Solution, TreeNode


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


class TestKthSmallestElementInABst(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_kth_smallest(self):
        cases = [
            # (level-order input, k, expected)
            ([3, 1, 4, None, 2], 1, 1),
            ([3, 1, 4, None, 2], 2, 2),
            ([3, 1, 4, None, 2], 4, 4),
            ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
            ([1], 1, 1),
        ]

        for values, k, expected in cases:
            with self.subTest(values=values, k=k):
                result = self.solution.kth_smallest(build_tree(values), k)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
