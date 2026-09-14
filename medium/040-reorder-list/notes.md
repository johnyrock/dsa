# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `reorder_list.py`, keep the tests, write it again.

## Key insight

The target order `L0, Ln, L1, Ln-1, ...` is the first half of the list interleaved with the *reversed* second half. So the problem decomposes into three standard linked-list moves: find the middle with slow/fast pointers, reverse the second half in place with the three-pointer loop, and merge the two halves by alternating one node from each. Cutting the first half (`slow.next = None`) before reversing is what makes the merge terminate cleanly, and the first half is never shorter than the second, so looping `while second` weaves everything.

## Complexity

- Time: O(n), three passes over at most n nodes each (half, half, half).
- Space: O(1), a handful of pointers; no array copy.

## Mistakes to watch for

- Forgetting `slow.next = None`. The first half then still runs through the old middle into the reversed tail, and the merge produces a cycle: `[1,2,3,4,5]` prints `1, 5, 2, 4, 3, 4, 3, 4, ...` forever.
- Assigning `second.next = first.next` *after* `first.next = second`. The saved successor is gone, `second.next` becomes `second` itself, and the list turns into `1 -> 5 -> 5 -> 5 -> ...`. Save `first_next` and `second_next` before rewiring anything.
- Using `while fast is not None and fast.next is not None` for the middle. `slow` then lands one node further right on even lengths (`[1,2,3,4]` splits as `[1,2,3]` / `[4]`). That still yields `[1,4,2,3]` here, but it is a different split from what the walkthrough narrates and it breaks the palindrome variant.
- Dropping the `head.next is None` guard. A one-node list works by accident, but an empty list dereferences `None.next` in the middle-finding loop.

## Related

- `easy/007-reverse-linked-list` — phase 2 verbatim; if you can write that from memory, this is two more loops.
- `easy/012-linked-list-cycle` — the slow/fast pointer walk used to find the middle.
- `medium/006-add-two-numbers` — another problem where the loop advances two list cursors together.
- Pattern doc: `../../patterns/linked-list.md`
