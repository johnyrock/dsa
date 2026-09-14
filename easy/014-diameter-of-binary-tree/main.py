from diameter_of_binary_tree import Solution, TreeNode

solution = Solution()

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(solution.diameter_of_binary_tree(root))
