# Notes

## Attempts

- 2026-09-05: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete the solution file, keep the tests, and write it again before trusting any confidence score.

## Key insight

Do not search for a pair of days. Walk forward and ask, at each day, "if I sold today, what is the most I could make?" The answer is `price - min_price_so_far`, and the minimum so far is one variable you update as you go. One pass, no pair search.

## Complexity

- Time: O(n), a single pass with O(1) work per day.
- Space: O(1), two scalars regardless of input size.

## Mistakes to watch for

- Start `best` at 0, not at negative infinity. A losing trade is never taken, so the answer is never negative.
- Update the minimum before considering a sale on the same day, and never let a buy day count as its own sell day.
- `[3, 2, 6, 5, 0, 3]` is the trap: the global minimum is 0 near the end, but the best trade (2 → 6, profit 4) finished long before it. Tracking the best profit separately from the minimum is what handles this.
- A single-element list must return 0, not crash.

## Related

- Best Time to Buy and Sell Stock II (LeetCode #122) allows unlimited transactions and collapses to summing every upward step.
- Maximum Subarray (LeetCode #53) is the same running-best trick applied to sums instead of differences.
