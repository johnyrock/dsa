# Notes

## Attempts

- 2026-09-05: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `climbing_stairs.py`, keep the tests, write it again.

## Key insight

The number of ways to reach step `n` is the number of ways to reach step `n - 1` (then take a 1-step) plus the number of ways to reach step `n - 2` (then take a 2-step). Since each answer depends only on the previous two, the whole dp table collapses into two rolling variables. It is the Fibonacci sequence shifted by one: 1, 2, 3, 5, 8, 13, ...

## Complexity

- Time: O(n), one pass from step 3 to step n.
- Space: O(1), only two integers are alive at any moment.

## Mistakes to watch for

- `n = 1` and `n = 2` need their own answers before the loop. Without the guard, `range(3, n + 1)` is empty and the seeded `one_back = 2` is returned for `n = 1`, which is wrong.
- Start the loop at 3, not 2. `range(2, n + 1)` does one extra iteration and returns the answer for `n + 1` (13 instead of 8 at `n = 5`).
- The tuple assignment `two_back, one_back = one_back, two_back + one_back` evaluates the right side first. Writing it as two separate statements clobbers `one_back` before it is used.
- Plain recursion without memoization is O(2^n) and times out well before `n = 45`.

## Related

- House Robber (medium) is the same recurrence shape with a max instead of a sum.
- Min Cost Climbing Stairs (easy, LeetCode #746) adds a per-step cost to the same table.
- Fibonacci Number (easy, LeetCode #509) is the identical loop with different base cases.
