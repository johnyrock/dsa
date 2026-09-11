# Notes

## Attempts

- 2026-09-12: Folder generated as reference material, not solved independently. First review should be a from-scratch re-solve: delete `kth_smallest_element_in_a_bst.py`, keep the tests, write it again.

## Key insight

An in-order traversal (left, node, right) of a BST visits nodes in strictly ascending value order — that's the BST invariant, restated as a traversal fact. So the k-th smallest value is simply the k-th node visited by an in-order walk. Doing it iteratively with an explicit stack lets the traversal stop the instant the k-th node is popped, instead of building the whole sorted list first.

## Complexity

- Time: O(h + k), h being the height to reach the leftmost node, then k more pops in the worst case.
- Space: O(h) for the stack.

## Mistakes to watch for

- Collecting the entire in-order sequence into a list and indexing `list[k-1]` — correct, but O(n) space and no early exit, wasteful when k is small.
- Decrementing `k` before checking `k == 0` vs after — get the order backwards and you're off by one on which node is returned.
- Recursive in-order without an early-return mechanism doesn't stop early; a global/nonlocal counter is needed, which is why the iterative stack version is usually cleaner here.

## Related

- Validate Binary Search Tree (medium) is the same in-order-is-sorted fact used to check ordering instead of finding a rank.
- Binary Search (easy) is the same "no need to build the whole structure to answer one query" instinct in a different shape.
