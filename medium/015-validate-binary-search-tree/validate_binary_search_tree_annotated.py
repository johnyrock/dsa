from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid_bst(self, root: TreeNode | None) -> bool:
        # Each recursive call carries the open interval (low, high) that this
        # node's value must fall inside, inherited from every ancestor above it —
        # not just its immediate parent, which is the mistake a naive
        # parent-only comparison makes.
        def valid(node, low, high):
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            # Going left tightens the upper bound to node.val; going right
            # tightens the lower bound. Both children inherit the untouched
            # other bound from this call.
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        return valid(root, float("-inf"), float("inf"))
