# 028. Longest Consecutive Sequence

**Difficulty:** Medium | **Pattern:** [hash-set](../../patterns/hash-set.md) ([explained](../../concepts/hash-map.html)) | **Source:** LeetCode #128

## Problem

You are given an unsorted integer array `nums`. Return the length of the longest run of consecutive integers that all appear in the array, regardless of where they sit in it. The values do not have to be adjacent in `nums`; `[100, 4, 200, 1, 3, 2]` contains the run 1, 2, 3, 4.

Your algorithm must run in O(n) time, which rules out sorting.

## Examples

```
Input:  nums = [100,4,200,1,3,2]
Output: 4             # 1, 2, 3, 4 are all present; 100 and 200 are runs of length 1

Input:  nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9             # 0 through 8; the duplicate 0 does not make the run longer

Input:  nums = []
Output: 0             # no values, no run
```

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from sorting to a set that lets each run be walked exactly once from its smallest value, with complexity.

## Follow-up

- Return the run itself (the list `[1, 2, 3, 4]`) rather than its length. What extra bookkeeping is needed, and does the complexity change?
- Suppose the values are bounded, say `0 <= nums[i] < 10^6`. Is there a version with a boolean array instead of a set, and when would it be worse?
- Binary Tree Longest Consecutive Sequence (LeetCode #298) asks the same question along root-to-leaf paths. Why does the "start of a run" trick not transfer, and what replaces it?
