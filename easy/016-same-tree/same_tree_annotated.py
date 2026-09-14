from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Compare both values and corresponding subtrees recursively.
    def is_same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # If either node is absent, they match only when both are absent.
        if p is None or q is None:
            return p is q
        # Equal roots need equal left and right subtrees too.
        return p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)
