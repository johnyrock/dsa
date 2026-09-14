# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `longest_increasing_subsequence.py`, keep the tests, write it again.

## Key insight

Anchor the subproblem on where the subsequence *ends*: `dp[i]` is the length of the longest increasing subsequence whose last element is `nums[i]`. Every element is a run of length 1 by itself, and `nums[i]` can extend any run ending at an earlier `j` with `nums[j] < nums[i]`, so `dp[i] = max(dp[i], dp[j] + 1)` over those `j`. The answer is `max(dp)`, not `dp[-1]`, because the best run can end anywhere.

## Complexity

- Time: O(n²), every `i` looks back at every `j < i`.
- Space: O(n) for the table.

## Mistakes to watch for

- Seeding `dp = [0] * n` instead of `[1] * n`. Then a run can never start: `dp[j] + 1` builds on zeros and the answer for `[10, 9, 2, 5, 3, 7, 101, 18]` comes out 0 instead of 4 (and `[1]` returns 0).
- Using `nums[j] <= nums[i]`. Equal values then chain, so `[7, 7, 7]` returns 3 instead of 1.
- Returning `dp[-1]` instead of `max(dp)`. The best run does not have to end at the last element: `[4, 5, 1]` returns 1 instead of 2.
- Reversing the order of the loops or filling `i` from the right: `dp[j]` must be final before `dp[i]` reads it, which only holds when `i` increases and `j < i`.

## Related

- [medium/008-coin-change](../008-coin-change/) has the same "look back at every earlier slot and take the best" shape.
- [easy/010-climbing-stairs](../../easy/010-climbing-stairs/) is the simplest table where each slot combines earlier slots.
- [medium/077-word-break](../077-word-break/) also scans every earlier index `j < i` for each `i`.
- [patterns/dynamic-programming.md](../../patterns/dynamic-programming.md)
