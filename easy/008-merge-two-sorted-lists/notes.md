# Notes

## Attempts

- 2026-09-05: Folder generated as reference material, not solved independently. The solution, the annotated version, and the walkthrough were written out rather than worked out, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `merge_two_sorted_lists.py`, keep the tests, write it again.

## Key insight

Both inputs are already sorted, so the smallest node not yet merged is always one of the two current heads. That turns merging into a single walk with one comparison per node, and no node ever has to be created or moved twice. A dummy head node removes the "is this the first node?" special case, so the loop body is the same on every iteration.

## Complexity

- Time: O(n + m), each node is visited and relinked exactly once.
- Space: O(1) extra, the nodes are spliced in place; only `dummy` and `tail` are allocated.

## Mistakes to watch for

- Forgetting `tail.next = list1 or list2` after the loop. The loop stops as soon as one list empties, and the remainder of the other is silently dropped.
- Not advancing `tail` after attaching, which leaves it pointing at an old node and overwrites the link on the next iteration.
- Returning `dummy` instead of `dummy.next`, which prepends a bogus 0.
- Using `<` instead of `<=` still returns a correctly sorted list, but it flips the order of equal values, so the merge is no longer stable.
- Assuming both lists are non-empty. Either can be `None`, and both can be.

## Related

- Merge k Sorted Lists (hard, #23) is this merge applied pairwise, or with a heap over the k heads.
- Merge Sorted Array (easy, #88) is the same merge on arrays, best done from the back to avoid shifting.
- The merge step of merge sort is exactly this function.
