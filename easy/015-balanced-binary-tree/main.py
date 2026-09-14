from balanced_binary_tree import Solution, TreeNode

solution = Solution()

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.is_balanced(root))
