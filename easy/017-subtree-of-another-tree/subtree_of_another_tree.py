from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_subtree(self, root: TreeNode | None, sub_root: TreeNode | None) -> bool:
        if sub_root is None:
            return True
        if root is None:
            return False
        return self._same_tree(root, sub_root) or self.is_subtree(root.left, sub_root) or self.is_subtree(root.right, sub_root)

    def _same_tree(self, first: TreeNode | None, second: TreeNode | None) -> bool:
        if first is None or second is None:
            return first is second
        return first.val == second.val and self._same_tree(first.left, second.left) and self._same_tree(first.right, second.right)
