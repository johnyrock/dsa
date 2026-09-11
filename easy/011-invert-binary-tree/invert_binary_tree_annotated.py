from __future__ import annotations


class TreeNode:
    # Same shape LeetCode gives you: a value and two optional children.
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert_tree(self, root: TreeNode | None) -> TreeNode | None:
        # An empty subtree mirrors to itself. This also stops the recursion at leaves,
        # whose left/right are None.
        if root is None:
            return None
        # Invert both subtrees first, then swap the (already-inverted) results into
        # the opposite slots. The right-hand side is evaluated before either
        # attribute is reassigned, so swapping in one line is safe.
        root.left, root.right = self.invert_tree(root.right), self.invert_tree(root.left)
        # Return the same node object, now mirrored, so the parent call can hang it
        # off the correct side.
        return root
