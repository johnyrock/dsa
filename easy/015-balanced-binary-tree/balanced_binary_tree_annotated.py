from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Decide balance while calculating each subtree height.
    def is_balanced(self, root: TreeNode | None) -> bool:
        # Return a height, or -1 as a sentinel for an unbalanced subtree.
        def height(node: TreeNode | None) -> int:
            # Empty subtrees have height zero and are balanced.
            if node is None:
                return 0
            # Check the left subtree first.
            left_height = height(node.left)
            # Propagate a failure without doing unnecessary work.
            if left_height == -1:
                return -1
            # Then obtain the right subtree height.
            right_height = height(node.right)
            # A failed child or a gap above one makes this subtree unbalanced.
            if right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            # A balanced node's height is one more than its taller child.
            return 1 + max(left_height, right_height)

        # Only the sentinel matters to the caller.
        return height(root) != -1
