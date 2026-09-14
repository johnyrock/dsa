from binary_tree_right_side_view import Solution, TreeNode

solution = Solution()

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
print(solution.right_side_view(root))

left_heavy = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
print(solution.right_side_view(left_heavy))
