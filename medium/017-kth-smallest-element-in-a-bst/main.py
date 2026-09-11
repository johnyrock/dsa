from kth_smallest_element_in_a_bst import Solution, TreeNode

root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(Solution().kth_smallest(root, 1))
