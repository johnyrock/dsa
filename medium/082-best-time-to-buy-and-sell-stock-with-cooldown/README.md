# 082. Best Time to Buy and Sell Stock with Cooldown

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #309

## Problem

You are given an array `prices` where `prices[i]` is the price of a stock on day `i`. You may complete as many buy-then-sell transactions as you like, but you can hold at most one share at a time, and after you sell you must skip the next day entirely (a one-day cooldown) before buying again.

Return the maximum profit you can achieve.

## Examples

```
Input:  prices = [1,2,3,0,2]
Output: 3             # buy 1, sell 2 (+1), rest on day 2, buy 0, sell 2 (+2); selling at 3 would block the buy at 0

Input:  prices = [1]
Output: 0             # one day, nothing to trade

Input:  prices = [2,1]
Output: 0             # the price only falls, so never buy
```

## Constraints

- `1 <= prices.length <= 5000`
- `0 <= prices[i] <= 1000`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from trying every sequence of trades to a three-state machine rolled forward one day at a time, with complexity.

## Follow-up

- Drop the cooldown (LeetCode #122). Which state disappears, and which single line of the recurrence changes?
- Add a transaction fee of `fee` per sale instead of the cooldown (LeetCode #714). Where does the fee go in the recurrence?
- Make the cooldown `k` days instead of one. How many states do you need, or can you keep three and read from `k` days back?
