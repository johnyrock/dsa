from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        index_of = {val: i for i, val in enumerate(inorder)}
        next_pre = 0

        def build(lo, hi):
            nonlocal next_pre
            if lo > hi:
                return None
            val = preorder[next_pre]
            next_pre += 1
            node = TreeNode(val)
            mid = index_of[val]
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(inorder) - 1)
