from __future__ import annotations
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Return the last node of every level, top to bottom, using a level-by-level breadth-first traversal.
    def right_side_view(self, root: TreeNode | None) -> list[int]:
        # An empty tree has no levels, so there is nothing to see. This guard also keeps the deque from starting with a None.
        if root is None:
            return []
        result = []
        # The queue holds exactly one level at a time when the loop below starts an iteration.
        queue = deque([root])
        while queue:
            # Freeze the level's size BEFORE popping. Children get appended during the loop, so len(queue) changes; this snapshot is what separates levels.
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                # The last node popped from this level is its rightmost, because children were appended left-to-right.
                if i == size - 1:
                    result.append(node.val)
                # Enqueue left before right so the next level's order is also left-to-right.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
