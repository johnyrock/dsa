from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def good_nodes(self, root: TreeNode | None) -> int:
        def dfs(node, max_so_far):
            if node is None:
                return 0
            count = 1 if node.val >= max_so_far else 0
            max_so_far = max(max_so_far, node.val)
            return count + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)

        return dfs(root, float("-inf"))
