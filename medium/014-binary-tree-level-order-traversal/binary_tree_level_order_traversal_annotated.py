from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        result = []
        # A queue gives FIFO order, which matches breadth-first traversal.
        queue = deque([root])
        while queue:
            level = []
            # Snapshot the queue's current length before the loop body starts
            # pushing next-level nodes into it — that's what separates one
            # level's nodes from the next level's.
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
