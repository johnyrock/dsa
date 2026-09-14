# 083. Coin Change II

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #518

## Problem

You are given an integer `amount` and an array `coins` of distinct coin denominations, with an unlimited supply of each. Two ways of making change count as the same combination if they use the same multiset of coins, regardless of order.

Return the number of combinations that add up to exactly `amount`, or `0` if none do. The answer fits in a 32-bit signed integer.

## Examples

```
Input:  amount = 5, coins = [1,2,5]
Output: 4             # 5, 2+2+1, 2+1+1+1, 1+1+1+1+1

Input:  amount = 3, coins = [2]
Output: 0             # 3 is odd, only even amounts are reachable

Input:  amount = 10, coins = [10]
Output: 1             # the single coin
```

## Constraints

- `1 <= coins.length <= 300`
- `1 <= coins[i] <= 5000`
- all the values of `coins` are unique
- `0 <= amount <= 5000`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from enumerating every multiset to a one-row table filled coin by coin, with complexity.

## Follow-up

- Swap the two loops (amounts outside, coins inside). What does the table count then, and which LeetCode problem is that (#377)?
- Each coin may be used at most once. Which direction must the inner loop run, and why?
- Count combinations modulo `10^9 + 7` for `amount` up to `10^5`. Does the algorithm change, or only the arithmetic?
