from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Search every root position where the smaller tree could begin.
    def is_subtree(self, root: TreeNode | None, sub_root: TreeNode | None) -> bool:
        # The empty tree is a subtree of every tree.
        if sub_root is None:
            return True
        # A nonempty candidate cannot fit into an empty tree.
        if root is None:
            return False
        # Either this root matches exactly, or a child subtree contains the match.
        return self._same_tree(root, sub_root) or self.is_subtree(root.left, sub_root) or self.is_subtree(root.right, sub_root)

    # Compare structures as well as values.
    def _same_tree(self, first: TreeNode | None, second: TreeNode | None) -> bool:
        # Missing children must appear in the same positions.
        if first is None or second is None:
            return first is second
        # Match the current values and recurse on both corresponding children.
        return first.val == second.val and self._same_tree(first.left, second.left) and self._same_tree(first.right, second.right)
