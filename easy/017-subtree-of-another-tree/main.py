from subtree_of_another_tree import Solution, TreeNode

solution = Solution()

root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
print(solution.is_subtree(root, TreeNode(4, TreeNode(1), TreeNode(2))))
