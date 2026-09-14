# 087. Jump Game II

**Difficulty:** Medium | **Pattern:** [greedy](../../patterns/greedy.md) ([explained](../../concepts/greedy.html)) | **Source:** LeetCode #45

## Problem

You are given a 0-indexed integer array `nums` and you start at index 0. From index `i` you may jump forward to any index in `i + 1 .. i + nums[i]`. The tests are built so that the last index is always reachable.

Return the minimum number of jumps needed to reach the last index.

## Examples

```
Input:  nums = [2,3,1,1,4]
Output: 2             # jump 1 step to index 1, then 3 steps to the last index

Input:  nums = [2,3,0,1,4]
Output: 2             # the 0 at index 2 does not matter, index 1 jumps straight over it

Input:  nums = [0]
Output: 0             # already standing on the last index
```

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- it is guaranteed that you can reach `nums[n - 1]`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from an O(n²) table of minimum jumps to a single sweep that advances a window one jump at a time, with complexity.

## Follow-up

- Drop the guarantee that the end is reachable: return `-1` when it is not, without a second pass.
- Return one optimal sequence of indices, not just its length. Which extra value per window do you need to remember?
- What if each `nums[i]` were a *fixed* jump length rather than a maximum? Is there still a greedy, or does it become a graph problem?
