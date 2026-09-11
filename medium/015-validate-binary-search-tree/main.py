from validate_binary_search_tree import Solution, TreeNode

solution = Solution()
print(solution.is_valid_bst(TreeNode(2, TreeNode(1), TreeNode(3))))
print(solution.is_valid_bst(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))))
