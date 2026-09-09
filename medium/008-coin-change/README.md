# 008. Coin Change

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #322

## Problem

You are given coin denominations `coins` and a target `amount`. Return the fewest coins needed to make exactly `amount`. You have an unlimited supply of each coin.

If the amount cannot be made from the given coins, return `-1`.

## Examples

```
Input:  coins = [1, 2, 5], amount = 11
Output: 3             # 5 + 5 + 1

Input:  coins = [2], amount = 3
Output: -1            # odd amounts are impossible with only 2s

Input:  coins = [1], amount = 0
Output: 0             # nothing to make, zero coins
```

## Constraints

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from the greedy that fails through the exponential recursion to the bottom-up table over amounts, with complexity.

## Follow-up

- Greedy (always take the largest coin) works for US coins. Find a coin set where it fails, and explain why the DP does not have that problem.
- How would you change the table to count the *number of ways* instead of the minimum coins? (LeetCode #518)
