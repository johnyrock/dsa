from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node:
            # BST ordering tells us which side both targets must be on without
            # searching: if both are smaller, the split point (and any LCA)
            # can only be further left.
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                # p and q are no longer both on the same side (one is <=
                # node.val, the other is >=, or one equals node.val itself) —
                # this is exactly where their paths diverge, the LCA.
                return node
        return None
