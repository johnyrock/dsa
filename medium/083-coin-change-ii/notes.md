# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the loop order argument.

## Key insight

`dp[a]` is the number of combinations that make amount `a` using only the coins processed so far, seeded with `dp[0] = 1` for the empty combination. For each coin, walk the amounts upward and add `dp[a - coin]` into `dp[a]`: every combination for `a - coin` gains one more of this coin. Putting the coin loop on the outside is what makes `{1, 2}` and `{2, 1}` a single combination, because a combination is only ever built in coin order. Walking amounts upward lets `dp[a - coin]` already contain this coin, which is the unlimited-supply rule.

## Complexity

- Time: O(len(coins) × amount), one addition per (coin, amount) pair.
- Space: O(amount) for the single row.

## Mistakes to watch for

- Loops in the wrong order (`for a in range(1, amount + 1): for coin in coins:`). That counts ordered sequences, so `1+2` and `2+1` are distinct; on `amount = 5`, `coins = [1,2,5]` it returns 9 instead of 4. It is the answer to Combination Sum IV, not this problem.
- Walking the inner loop downward (`range(amount, coin - 1, -1)`). Then `dp[a - coin]` has not yet been updated for this coin, so each coin is used at most once: `amount = 5`, `coins = [1,2,5]` gives 1 (only the single 5) instead of 4.
- Seeding `dp[0] = 0`. Nothing ever becomes nonzero and every answer is 0.
- Starting the inner loop at `range(1, ...)` instead of `range(coin, ...)`; `dp[a - coin]` then goes negative and wraps around to the end of the list in Python, quietly adding garbage.

## Related

- [medium/008-coin-change](../008-coin-change) is the same table asking for the minimum number of coins instead of the number of combinations; its loop order does not matter, this one's does.
- [medium/084-target-sum](../084-target-sum) is the each-item-once version of counting subsets, with the inner loop running downward.
- [easy/010-climbing-stairs](../../easy/010-climbing-stairs) counts ordered sequences of steps of size 1 or 2, which is what the swapped-loop bug computes here.
- Review the [Dynamic Programming pattern](../../patterns/dynamic-programming.md) and its concept page.
