from __future__ import annotations


class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clone_graph(self, node: Node | None) -> Node | None:
        if node is None:
            return None

        # Maps original node -> its clone. This both avoids infinite recursion
        # on cycles and ensures each original node gets exactly one clone,
        # even when reached through multiple paths.
        clones = {}

        def dfs(n):
            # Already cloned (possibly still under construction, if we're on
            # a cycle) — return the existing clone instead of recursing again.
            if n in clones:
                return clones[n]
            copy = Node(n.val)
            # Register the clone before recursing into neighbors, so that a
            # cycle back to `n` finds this entry instead of looping forever.
            clones[n] = copy
            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)
