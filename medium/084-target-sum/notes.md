# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and re-derive the subset-sum reduction.

## Key insight

Split the numbers into the plus group `P` and the minus group `N`. Then `P - N = target` and `P + N = total`, so `P = (total + target) / 2`: every valid expression is exactly one subset whose sum is that `goal`. Count subsets with a 0/1 knapsack row: `dp[s]` is the number of subsets of the numbers so far that sum to `s`, seeded `dp[0] = 1`, and for each number the sums are walked *downward* with `dp[s] += dp[s - num]`, so each number joins a subset at most once. If `total + target` is odd or `|target| > total`, no subset can work and the answer is 0.

## Complexity

- Time: O(n × goal), with goal at most `sum(nums)`, so at most 20 × 1000 additions.
- Space: O(goal) for the single row.

## Mistakes to watch for

- Walking the inner loop upward (`range(num, goal + 1)`). Then `dp[s - num]` already includes this same number, so it can be reused: `[1,1,1,1,1]`, `target = 3` returns 70 (multisets of 1s) instead of 5.
- Skipping the parity check. `(total + target) // 2` silently rounds down, so `[1,2,3]`, `target = 1` computes `goal = 3` and returns 2 instead of 0.
- Forgetting `abs(target) > total`. A large negative target makes `goal` negative, and `[0] * (goal + 1)` is an empty list, so `dp[0] = 1` raises `IndexError`.
- Treating zeros specially. A 0 can take either sign and both count as different expressions; the DP handles that on its own because `dp[s] += dp[s - 0]` doubles every count, but a "skip zeros" shortcut drops those doublings and returns 1 instead of 256 for eight zeros and a 1.

## Related

- [medium/083-coin-change-ii](../083-coin-change-ii) is the unlimited-supply version of the same row, with the inner loop running upward instead of downward.
- [medium/079-partition-equal-subset-sum](../079-partition-equal-subset-sum) is the same reduction with a boolean row: can any subset hit `total / 2`?
- [medium/053-subsets](../053-subsets) enumerates the subsets this problem counts.
- Review the [Dynamic Programming pattern](../../patterns/dynamic-programming.md) and its concept page.
