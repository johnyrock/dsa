# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete `find_the_duplicate_number.py`, and rebuild Floyd's two phases from the "array as linked list" picture.

## Key insight

Read the array as a function `i -> nums[i]`. Since every value is in `[1, n]` and there are `n + 1` indices, following that function from index 0 must eventually revisit an index, and the index it re-enters is one that two different indices point to: the duplicate value. So the problem is Linked List Cycle II on an implicit list. Floyd's phase 1 (slow one hop, fast two hops, until equal) finds *a* point on the cycle; phase 2 (restart one pointer at 0, walk both at speed 1) finds the *entrance*, which is the answer. Index 0 is never a target because values are at least 1, so the start is guaranteed to be outside the cycle.

## Complexity

- Time: O(n). Phase 1 takes at most a cycle-length-plus-tail number of steps; phase 2 at most the tail length.
- Space: O(1), three integers. The array is read but never written.

## Mistakes to watch for

- Writing phase 1 as `while slow != fast:` with `slow = fast = 0`. The condition is false before the first hop, the loop body never runs, phase 2 then starts with `slow == slow2 == 0`, and the function returns `0` for `[1,3,4,2,2]`. Use a `while True` / `break` (do-while) shape, or take one hop before the loop.
- Returning the phase-1 meeting point. On `[1,3,4,2,2]` slow and fast first meet at index 4, but the duplicate is 2; the meeting point is only somewhere on the cycle.
- Starting phase 2's second pointer at `slow` (or moving it two hops). The distance argument requires one pointer at index 0 and both moving one hop; anything else does not land on the entrance.
- Starting the pointers at `nums[0]` instead of `0`. `nums[0]` may itself be on the cycle, and then the start is not "outside" the cycle, breaking the equal-distance argument; `[3,3,3,3,3]` still works by luck, but the general proof does not.

## Related

- [easy/012-linked-list-cycle](../../easy/012-linked-list-cycle) is phase 1 of this algorithm on a real linked list.
- [easy/022-happy-number](../../easy/022-happy-number) uses the same slow/fast pointers on an implicit function (digit-square sum) instead of an array.
- [easy/028-missing-number](../../easy/028-missing-number) is the mirror problem: one value from `[0, n]` is absent instead of repeated.
- Review the [Fast & Slow Pointers pattern](../../patterns/fast-slow-pointers.md) and its concept page.
