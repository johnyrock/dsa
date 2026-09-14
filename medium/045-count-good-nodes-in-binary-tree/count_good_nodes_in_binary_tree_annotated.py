from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Count the nodes X such that no node on the path from the root to X has a value greater than X.val.
    def good_nodes(self, root: TreeNode | None) -> int:
        # The helper carries the largest value seen on the root-to-node path so far; that is the only fact a node needs to decide if it is good.
        def dfs(node, max_so_far):
            # An empty subtree contributes no good nodes; this is also what stops the recursion at the leaves' missing children.
            if node is None:
                return 0
            # A node is good when it is at least as large as everything above it. ">=" not ">": a value equal to the path max still counts (the root's duplicate 3 in the example is good).
            count = 1 if node.val >= max_so_far else 0
            # Update the path max before recursing so the children compare against this node too. Reassigning the local parameter does not affect the sibling call, which gets the parent's value.
            max_so_far = max(max_so_far, node.val)
            # This node's own count plus whatever the two subtrees report, each given the updated path maximum.
            return count + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)

        # The root has no ancestors, so seed the max with -inf: the root is always good.
        return dfs(root, float("-inf"))
