# Notes

## Attempts

- 2026-09-04: Asked for the answer directly after seeing the problem. Reviewed the O(n) hash map solution and an annotated version. Backfilled from chat, so no independent solve yet. Re-solve on next review before trusting the confidence score.

## Key insight

Instead of searching for a pair, flip the question: for each number, ask whether its complement (`target - n`) has already been seen. A dict answers that in O(1), so one pass is enough.

## Complexity

- Time: O(n), one pass with O(1) lookups.
- Space: O(n) for the dict in the worst case.

## Mistakes to watch for

- Insert into `seen` after the check, not before, or an element can pair with itself.
- Return the earlier index first: `[seen[complement], i]`.

## Related

- 3Sum (medium) builds on this with sorting plus two pointers.
- Two Sum II (sorted input) is a two-pointers problem, not a hash map one.
