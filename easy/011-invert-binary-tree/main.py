from invert_binary_tree import Solution, TreeNode

solution = Solution()

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
inverted = solution.invert_tree(root)


def preorder(node):
    if node is None:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)


print(preorder(inverted))
