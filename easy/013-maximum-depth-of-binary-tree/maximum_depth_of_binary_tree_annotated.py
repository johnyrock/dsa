from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Return the number of nodes on the longest root-to-leaf path.
    def max_depth(self, root: TreeNode | None) -> int:
        # An empty subtree contributes no levels.
        if root is None:
            return 0
        # Count this node after recursively finding each child's maximum depth.
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
