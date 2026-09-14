from count_good_nodes_in_binary_tree import Solution, TreeNode

solution = Solution()
root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
print(solution.good_nodes(root))
print(solution.good_nodes(TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))))
