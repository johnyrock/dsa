# 057. Combination Sum II

**Difficulty:** Medium | **Pattern:** [backtracking](../../patterns/backtracking.md) ([explained](../../concepts/backtracking.html)) | **Source:** LeetCode #40

## Problem

Given a list of integers `candidates` (which may contain repeated values) and an integer `target`, return every distinct combination of candidates whose values add up to `target`. Each element of `candidates` may be used at most once in a combination, and two combinations are the same if they hold the same multiset of numbers regardless of order.

Return the list of combinations in any order, with no duplicate combinations.

## Examples

```
Input:  candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]   # both 1s may be used together, but [1,7] appears once, not once per 1

Input:  candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]                   # three 2s exist but only two are needed; [2,2,1] is the same combination as [1,2,2]

Input:  candidates = [3], target = 8
Output: []                              # 3 cannot be reused, so nothing reaches 8
```

## Constraints

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from generating every subset to a sorted backtracking with a duplicate skip and an early break, with complexity.

## Follow-up

- Combination Sum I (LeetCode #39) lets each candidate be reused. Which single character of the recursive call changes, and why does the duplicate-skip line then become unnecessary?
- Instead of the `i > start` skip, count each distinct value and branch on "use 0, 1, ..., count copies". How does the tree shape change and is it fewer calls?
- Suppose `target` could be up to 10^4 and you only need the *number* of combinations, not the lists. Which technique replaces backtracking?
