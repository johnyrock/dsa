# 053. Subsets

**Difficulty:** Medium | **Pattern:** [backtracking](../../patterns/backtracking.md) ([explained](../../concepts/backtracking.html)) | **Source:** LeetCode #78

## Problem

Given an array `nums` of distinct integers, return every possible subset of it (the power set): every way of choosing none, some, or all of its elements.

The output may be in any order, but it must not contain duplicate subsets. `[1, 2]` and `[2, 1]` count as the same subset.

## Examples

```
Input:  nums = [1, 2, 3]
Output: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]   # 2^3 = 8 subsets, each in index order

Input:  nums = [0]
Output: [[], [0]]                                            # the empty set and the whole set

Input:  nums = [4, 7]
Output: [[], [4], [4,7], [7]]                                # [7,4] must not appear alongside [4,7]
```

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- all the numbers of `nums` are unique

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from counting subsets in binary to a recursion that records every prefix and only ever extends it with later elements, with the recursion tree drawn alongside.

## Follow-up

- Only subsets of exactly size `k` are wanted (LeetCode #77, Combinations). Which single line changes, and how many recursion nodes are skipped?
- `nums` may now contain duplicates and the output must still have no repeated subsets (LeetCode #90, Subsets II). What extra condition inside the loop handles it, and why must the array be sorted first?
- Produce the subsets iteratively, without recursion, by doubling the result list once per element. What is the space cost beyond the output, and why can't that version prune?
