from lowest_common_ancestor_of_a_bst import Solution, TreeNode

n2, n8 = TreeNode(2), TreeNode(8)
root = TreeNode(6, n2, n8)
solution = Solution()
print(solution.lowest_common_ancestor(root, n2, n8).val)
