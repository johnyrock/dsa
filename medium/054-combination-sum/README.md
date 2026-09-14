# 054. Combination Sum

**Difficulty:** Medium | **Pattern:** [backtracking](../../patterns/backtracking.md) ([explained](../../concepts/backtracking.html)) | **Source:** LeetCode #39

## Problem

Given an array `candidates` of distinct positive integers and a `target`, return every combination of candidates whose sum is exactly `target`. Each candidate may be used any number of times.

Two combinations are the same if they use the same candidates the same number of times, so `[2, 2, 3]` and `[3, 2, 2]` must appear only once. The output may be in any order.

## Examples

```
Input:  candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]                       # 2+2+3 = 7 and 7 = 7; 2 is reused

Input:  candidates = [2, 3, 5], target = 8
Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]      # one candidate used four times

Input:  candidates = [2], target = 1
Output: []                                     # nothing fits
```

## Constraints

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- all elements of `candidates` are distinct
- `1 <= target <= 40`
- the number of unique combinations is fewer than 150

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from trying a count for every candidate to a recursion that spends candidates in index order, reuses them by recursing from the same index, and breaks as soon as one overshoots, with the recursion tree drawn alongside.

## Follow-up

- Each candidate may now be used at most once and the input may contain duplicates (LeetCode #40, Combination Sum II). Which two lines change?
- You only need the *number* of combinations, not the lists, and order does not matter. Which dynamic-programming table answers that in O(n · target), and why must the outer loop be over candidates rather than over the target?
- What if the order of picks *did* matter, so `[2, 2, 3]` and `[3, 2, 2]` are different (LeetCode #377)? What happens to the `start` index, and why does the count explode?
