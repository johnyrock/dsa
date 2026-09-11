from binary_tree_level_order_traversal import Solution, TreeNode

solution = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.level_order(root))
