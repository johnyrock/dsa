# 056. Subsets II

**Difficulty:** Medium | **Pattern:** [backtracking](../../patterns/backtracking.md) ([explained](../../concepts/backtracking.html)) | **Source:** LeetCode #90

## Problem

Given an array `nums` that may contain duplicate values, return every distinct subset of it (the power set without repeated subsets).

The output may be in any order, but two subsets that contain the same values the same number of times count as the same subset and must appear only once. `[2, 2]`, using both copies of a repeated value, is a legitimate subset.

## Examples

```
Input:  nums = [1, 2, 2]
Output: [[], [1], [1,2], [1,2,2], [2], [2,2]]   # 6 subsets; plain Subsets would give 8 with [1,2] and [2] twice

Input:  nums = [0]
Output: [[], [0]]

Input:  nums = [4, 4, 4, 1]
Output: [[], [1], [1,4], [1,4,4], [1,4,4,4], [4], [4,4], [4,4,4]]   # sorted first; each count of 4 appears once
```

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from generating every subset and deduplicating afterwards to a sort plus a one-line skip that never builds a duplicate, with the recursion tree drawn alongside and the pruned branches marked.

## Follow-up

- Apply the same sort-and-skip idea to permutations of an array with duplicates (LeetCode #47). Why does the condition there need `not used[i - 1]` as well?
- Combination Sum II (LeetCode #40) uses the identical `i > start and nums[i] == nums[i - 1]` skip. What is different about its base case and its recursive index?
- Can you produce the distinct subsets without sorting, by counting each value and choosing how many copies (0 to count) to include? What is the recursion tree's shape then?
