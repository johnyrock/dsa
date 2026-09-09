# 005. Best Time to Buy and Sell Stock

**Difficulty:** Easy | **Pattern:** [sliding-window](../../patterns/sliding-window.md) ([explained](../../concepts/sliding-window.html)) | **Source:** LeetCode #121

## Problem

Given an array `prices` where `prices[i]` is the price of a stock on day `i`, pick one day to buy and a later day to sell, and return the largest profit you can make.

You must buy before you sell. If no pair of days produces a profit, return `0`.

## Examples

```
Input:  prices = [7, 1, 5, 3, 6, 4]
Output: 5             # buy on day 1 at 1, sell on day 4 at 6

Input:  prices = [7, 6, 4, 3, 1]
Output: 0             # prices only fall, so no trade is better than no trade

Input:  prices = [2, 4, 1]
Output: 2             # buy at 2, sell at 4; the later 1 is too late to help
```

## Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`
- the sell day must come strictly after the buy day

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from brute force to the one-pass minimum tracker, with complexity.

## Follow-up

- The brute force is O(n²). Can you do it in one pass?
- What changes if you are allowed to buy and sell as many times as you like? (LeetCode #122)
