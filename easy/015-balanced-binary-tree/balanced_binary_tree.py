from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_balanced(self, root: TreeNode | None) -> bool:
        def height(node: TreeNode | None) -> int:
            if node is None:
                return 0
            left_height = height(node.left)
            if left_height == -1:
                return -1
            right_height = height(node.right)
            if right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return 1 + max(left_height, right_height)

        return height(root) != -1
