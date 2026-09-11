# Notes

## Attempts

- 2026-09-12: Folder generated as reference material, not solved independently. First review should be a from-scratch re-solve: delete `serialize_and_deserialize_binary_tree.py`, keep the tests, write it again.

## Key insight

A pre-order traversal alone doesn't uniquely determine a tree's shape — but a pre-order traversal that also writes an explicit marker (`"N"`) for every `None` child does. Every internal decision ("does this node have a left child? a right child?") is recorded in the stream, so `deserialize` can rebuild the exact structure by consuming tokens in the same order they were written, one recursive call per subtree.

## Complexity

- Time: O(n) for both serialize and deserialize.
- Space: O(n) for the encoded string, plus O(h) recursion depth.

## Mistakes to watch for

- Serializing without null markers (e.g. just the values in pre-order) — ambiguous, since different tree shapes can share the same pre-order value sequence.
- In `deserialize`, using an index variable that has to be manually incremented instead of an iterator — easy to forget a `+= 1` on one branch and desync the reads.
- Building `left` and `right` out of order relative to how they were serialized (pre-order write must be pre-order read: node, then left, then right).

## Related

- Binary Tree Level Order Traversal (medium) offers an alternative encoding (BFS with null markers) with different trade-offs (wider strings for sparse trees, no recursion needed to decode).
- Construct Binary Tree from Preorder and Inorder Traversal (medium, LeetCode #105) rebuilds a tree from two traversals instead of one traversal plus null markers.
