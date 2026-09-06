# Notes

## Attempts

- 2026-09-06: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete `coin_change.py`, keep the tests, write it again.

## Key insight

Think about the *last* coin in an optimal pile for amount `a`. It is some coin `c`, and the rest of the pile is an optimal pile for `a - c`. So `dp[a] = 1 + min(dp[a - c] for every c that fits)`. Fill a table from 0 upward and every `dp[a - c]` you need is already final. Greedy fails because taking the biggest coin now can force more coins later; the table considers every last coin.

## Complexity

- Time: O(amount × len(coins)). One slot per amount, one try per coin.
- Space: O(amount) for the table.

## Mistakes to watch for

- Greedy. `coins = [1, 3, 4], amount = 6`: greedy takes 4 + 1 + 1 = 3 coins, the answer is 3 + 3 = 2.
- Using `float("inf")` and then doing arithmetic on it. It works in Python, but `amount + 1` is a cleaner sentinel and stays an int.
- Forgetting `dp[0] = 0`. Without the base case nothing is ever reachable.
- Checking `c <= a` after indexing `dp[a - c]`, which goes negative and silently reads from the end of the list in Python.
- Returning `dp[amount]` without mapping the sentinel back to `-1`.
- Top-down memoised recursion is equally valid and sometimes more natural; just remember the cache, or it is exponential.

## Related

- Climbing Stairs (easy/010) is the same "build amount a from smaller amounts" table with steps instead of coins and counting instead of minimising.
- Coin Change II (LeetCode #518) counts combinations; the loop order over coins and amounts flips so each combination is counted once.
- Perfect Squares (LeetCode #279) is Coin Change with the coins being the square numbers.
