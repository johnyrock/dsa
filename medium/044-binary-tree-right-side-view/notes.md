# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete `binary_tree_right_side_view.py`, and rebuild the level-order loop.

## Key insight

"Visible from the right" means "last node of its level", not "reachable by going right". A level-order (BFS) traversal that snapshots `size = len(queue)` at the start of each level pops exactly that level's nodes in left-to-right order, so the node popped at `i == size - 1` is the rightmost one. Appending `node.left` before `node.right` keeps the next level ordered the same way. The answer is one value per level, so its length equals the tree's height.

## Complexity

- Time: O(n), each node is enqueued and dequeued once.
- Space: O(w) for the queue, where w is the widest level (up to n/2 for a complete tree).

## Mistakes to watch for

- Checking `i == len(queue) - 1` inside the loop instead of against the frozen `size`. Children appended during the level change `len(queue)`, so the test fires on the wrong node: `[1,2,3,null,5,null,4]` returns `[3, 5]` (the root is skipped, and 5 is reported instead of 4).
- Following only `root.right` down the tree. That returns `[1, 3, 4]` on the example by luck, but `[1,2,3,4,null,null,null,5]` gives `[1, 3]` instead of `[1, 3, 4, 5]`, because depths 2 and 3 exist only in the left subtree.
- Recording `i == 0` instead of `i == size - 1`. That is the *left* side view: `[1, 2, 5]` on the example.
- Enqueuing `node.right` before `node.left`. Then the last node popped at each level is the leftmost, and the example again yields `[1, 2, 5]`.

## Related

- [medium/014-binary-tree-level-order-traversal](../014-binary-tree-level-order-traversal) is the same loop, collecting the whole level instead of its last node.
- [easy/013-maximum-depth-of-binary-tree](../../easy/013-maximum-depth-of-binary-tree) computes the length of this answer (one entry per level).
- [medium/023-serialize-and-deserialize-binary-tree](../023-serialize-and-deserialize-binary-tree) also walks the tree in level order with a queue.
- Review the [Tree pattern](../../patterns/tree.md) and its concept page.
