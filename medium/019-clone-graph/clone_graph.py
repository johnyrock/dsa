from __future__ import annotations


class Node:
    def __init__(self, val: int = 0, neighbors: list[Node] | None = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def clone_graph(self, node: Node | None) -> Node | None:
        if node is None:
            return None

        clones = {}

        def dfs(n):
            if n in clones:
                return clones[n]
            copy = Node(n.val)
            clones[n] = copy
            for neighbor in n.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)
