# 086. Jump Game

**Difficulty:** Medium | **Pattern:** [greedy](../../patterns/greedy.md) ([explained](../../concepts/greedy.html)) | **Source:** LeetCode #55

## Problem

You are given an integer array `nums` and you start at index 0. The value `nums[i]` is the maximum jump length you can take forward from index `i` (any shorter jump is allowed too).

Return `true` if you can reach the last index, and `false` otherwise.

## Examples

```
Input:  nums = [2,3,1,1,4]
Output: true          # jump 1 step from index 0 to 1, then 3 steps to the last index

Input:  nums = [3,2,1,0,4]
Output: false         # every route lands on index 3, whose jump length is 0

Input:  nums = [0]
Output: true          # you are already standing on the last index
```

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from exploring every jump to a single `reach` frontier swept left to right, with complexity.

## Follow-up

- Instead of yes/no, return the minimum number of jumps needed (Jump Game II, [medium/087](../087-jump-game-ii)).
- Suppose you can jump backwards as well as forwards by up to `nums[i]`. Does the single-pass frontier still work, or do you need a graph search?
- Can you return the actual sequence of indices visited, not just whether one exists?
