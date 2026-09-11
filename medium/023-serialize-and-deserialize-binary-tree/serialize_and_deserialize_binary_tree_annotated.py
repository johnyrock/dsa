from __future__ import annotations


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        values = []

        # Pre-order (node, left, right) with an explicit "N" marker for every
        # None child. The marker is what makes the shape reconstructible: it
        # tells deserialize exactly where each subtree stops.
        def dfs(node):
            if node is None:
                values.append("N")
                return
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(values)

    def deserialize(self, data: str) -> TreeNode | None:
        # An iterator lets each recursive call consume exactly the tokens its
        # own subtree needs, leaving the rest for the caller — no index
        # bookkeeping required.
        values = iter(data.split(","))

        def build():
            val = next(values)
            if val == "N":
                return None
            node = TreeNode(int(val))
            # Rebuild left before right, mirroring the pre-order write order —
            # each call consumes tokens in the same sequence they were emitted.
            node.left = build()
            node.right = build()
            return node

        return build()
