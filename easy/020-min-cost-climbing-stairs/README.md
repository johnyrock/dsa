# 020. Min Cost Climbing Stairs

**Difficulty:** Easy | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #746

## Problem

You are given an array `cost` where `cost[i]` is the price of stepping *on* stair `i`. Once you have paid for a stair you may climb 1 or 2 stairs further. You may start on stair 0 or stair 1, and the top of the staircase is one past the last index.

Return the minimum total cost to reach the top.

## Examples

```
Input:  cost = [10,15,20]
Output: 15            # start on stair 1 (pay 15), jump two to the top

Input:  cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6             # start on 0, then indices 2, 4, 6, 7, 9: 1+1+1+1+1+1

Input:  cost = [5,7]
Output: 5             # start on stair 0 and jump straight over stair 1
```

## Constraints

- `2 <= cost.length <= 1000`
- `0 <= cost[i] <= 999`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the brute-force idea, invariant, trace, pitfalls, and complexity.

## Follow-up

- Can you recover the actual sequence of stairs taken, not just the cost? What extra state does that require?
- What changes if you must start on stair 0 (no free choice of stair 1)? Which initial value moves?
- What if each move can be 1, 2, or 3 stairs? Rewrite the two-variable loop for three.
