from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kth_smallest(self, root: TreeNode | None, k: int) -> int:
        # In-order traversal of a BST visits values in ascending order, so the
        # k-th value visited is the k-th smallest — no need to collect all of
        # them into a list first.
        stack = []
        node = root
        while stack or node:
            # Push every left descendant before visiting anything, exactly
            # like manual in-order recursion would.
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            # This is the k-th node visited in ascending order — stop early
            # instead of walking the rest of the tree.
            if k == 0:
                return node.val
            node = node.right
        return -1
