from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameter_of_binary_tree(self, root: TreeNode | None) -> int:
        diameter = 0

        def height(node: TreeNode | None) -> int:
            nonlocal diameter
            if node is None:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            diameter = max(diameter, left_height + right_height)
            return 1 + max(left_height, right_height)

        height(root)
        return diameter
