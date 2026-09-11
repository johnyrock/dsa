# Notes

## Attempts

- 2026-09-12: Folder generated as reference material, not solved independently. First review should be a from-scratch re-solve: delete `binary_tree_level_order_traversal.py`, keep the tests, write it again.

## Key insight

A plain BFS queue naturally visits nodes in level order, but it doesn't know where one level ends and the next begins unless you track it. Snapshotting `len(queue)` at the start of each level's loop draws that boundary: process exactly that many nodes (this level's), and anything pushed during that processing belongs to the next level.

## Complexity

- Time: O(n), every node is enqueued and dequeued once.
- Space: O(n) for the queue (worst case, the last level of a complete tree holds ~n/2 nodes) plus O(n) for the output.

## Mistakes to watch for

- Recomputing `len(queue)` inside the inner loop instead of snapshotting it before the loop starts — the length changes as children are pushed, which merges levels together.
- Using DFS (recursion) with a depth parameter also works but is a different pattern; don't reach for it out of habit when BFS is the natural fit.
- Forgetting the `root is None` base case, which would try to seed the queue with `None`.

## Related

- Invert Binary Tree (easy) traverses the same shape depth-first instead.
- Binary Tree Zigzag Level Order Traversal (medium, LeetCode #103) is this same BFS with alternating level order reversed.
