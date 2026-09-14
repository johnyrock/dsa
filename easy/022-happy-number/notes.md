# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

The digit-square map turns `n` into a linked list where each value's `next` is computed instead of stored. Since a 10-digit number maps to at most `10 * 81 = 810`, every sequence quickly drops into a small range and must either hit `1` (which maps to itself) or repeat a value, i.e. enter a cycle. That is exactly the Linked List Cycle setup, so `slow` advances one step and `fast` two; the loop ends when `fast == 1` (happy) or `slow == fast` (stuck in a cycle that is not `1`).

## Complexity

- Time: O(log n) per `_next` call (one iteration per digit), and the number of steps before reaching `1` or a repeat is bounded by a small constant once the value drops below 1000, so O(log n) overall.
- Space: O(1), two integers instead of a visited set.

## Mistakes to watch for

- Starting `fast = n` together with `slow = n`. Then `slow == fast` is true before the first step and `while` exits immediately, returning `n == 1`. `fast` must begin one step ahead.
- Checking `slow == 1` instead of `fast == 1` in the loop condition. `fast` reaches `1` first, and because `1` maps to `1` it stays there, so `fast` is the one that signals success early.
- Writing `_next` with string conversion (`sum(int(d) ** 2 for d in str(n))`) is fine, but `digit ** 2` on the `divmod` remainder must use the *digit*, not the shrinking `value`.
- Returning `slow == fast` or `True` after the loop. The loop also exits on `slow == fast` for cycles, so the only correct return is `fast == 1`.

## Related

- [easy/012-linked-list-cycle](../../easy/012-linked-list-cycle/) is the same tortoise-and-hare loop on real `next` pointers instead of a computed function.
- [easy/003-contains-duplicate](../../easy/003-contains-duplicate/) is the visited-set idea this solution replaces.
- Linked List Cycle II (medium, LeetCode #142) extends the two runners to locate where the cycle begins.
- Pattern doc: [fast-slow-pointers](../../patterns/fast-slow-pointers.md).
