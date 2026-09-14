from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Rebuild the unique binary tree whose preorder and inorder traversals are the two given lists (values are distinct).
    def build_tree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # Map each value to its inorder position once, so splitting the inorder window around a root is O(1) instead of a linear search.
        index_of = {val: i for i, val in enumerate(inorder)}
        # Preorder lists every root before its subtrees, so a single cursor walking left to right hands out the next root each time build() is called.
        next_pre = 0

        # build(lo, hi) returns the subtree whose inorder values are inorder[lo..hi] inclusive.
        def build(lo, hi):
            nonlocal next_pre
            # An empty inorder window is an empty subtree. This is also what keeps the preorder cursor from running past the end.
            if lo > hi:
                return None
            # The next unconsumed preorder value is the root of this window, because preorder visits root first and the calls happen in preorder order.
            val = preorder[next_pre]
            # Advance the cursor before recursing, so the left subtree's build() call sees the value after this root.
            next_pre += 1
            node = TreeNode(val)
            # Where the root sits in inorder: everything to its left is the left subtree, everything to its right is the right subtree.
            mid = index_of[val]
            # Build the left subtree first. Order matters: preorder lists the whole left subtree before the right one, so left must consume its preorder values first.
            node.left = build(lo, mid - 1)
            # Only then the right subtree, which starts wherever the cursor now stands.
            node.right = build(mid + 1, hi)
            return node

        # The whole tree covers the whole inorder list.
        return build(0, len(inorder) - 1)
