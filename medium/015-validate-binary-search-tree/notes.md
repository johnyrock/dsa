# Notes

## Attempts

- 2026-09-12: Folder generated as reference material, not solved independently. First review should be a from-scratch re-solve: delete `validate_binary_search_tree.py`, keep the tests, write it again.

## Key insight

Comparing a node only to its immediate parent isn't enough — a node must satisfy the constraint from *every* ancestor above it, not just the one directly above. Carry an open interval `(low, high)` down through the recursion: going left tightens `high` to the current node's value, going right tightens `low`. A node is valid only if it falls strictly inside the interval it inherited.

## Complexity

- Time: O(n), every node is visited once.
- Space: O(h) for the call stack, h being the tree's height.

## Mistakes to watch for

- Comparing each node only against its direct parent — passes `[5,1,4,null,null,3,6]` incorrectly, since 4 > 1 and 3 < 4 look locally fine, but 3 is in 5's right subtree and must be > 5.
- Using `<=`/`>=` instead of strict `<`/`>` — a BST with duplicate values is invalid.
- Using a sentinel like `float('-inf')`/`float('inf')` is fine in Python; in other languages, watch for integer overflow if using `INT_MIN`/`INT_MAX` as the initial bounds when node values can equal them.

## Related

- Kth Smallest Element in a BST (medium) exploits the same in-order-is-sorted property from the other direction.
- Lowest Common Ancestor of a BST (medium) uses BST ordering to prune the search instead of validating it.
