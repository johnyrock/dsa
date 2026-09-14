from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Return the longest path between any two nodes, measured in edges.
    def diameter_of_binary_tree(self, root: TreeNode | None) -> int:
        # Keep the best path seen while the post-order traversal computes heights.
        diameter = 0

        # Return a subtree's height while updating paths that pass through this node.
        def height(node: TreeNode | None) -> int:
            # The nested helper updates the answer owned by the outer method.
            nonlocal diameter
            # An empty child has height zero.
            if node is None:
                return 0
            # Compute child heights before combining them at this node.
            left_height = height(node.left)
            right_height = height(node.right)
            # A path through this node uses the left and right edge counts together.
            diameter = max(diameter, left_height + right_height)
            # Its parent only needs this subtree's longest downward path.
            return 1 + max(left_height, right_height)

        # Visit every node once.
        height(root)
        # The side effect accumulated the global best path.
        return diameter
