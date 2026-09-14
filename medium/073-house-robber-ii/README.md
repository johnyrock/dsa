# 073. House Robber II

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #213

## Problem

You are a robber planning to rob houses arranged in a circle: `nums[i]` is the money in house `i`, and the first and last houses are neighbours. Adjacent houses share an alarm, so you cannot rob two houses that are next to each other.

Return the maximum amount of money you can rob without triggering the alarm.

## Examples

```
Input:  nums = [2, 3, 2]
Output: 3             # houses 0 and 2 are neighbours on the circle, so 2 + 2 is illegal; take the 3

Input:  nums = [1, 2, 3, 1]
Output: 4             # house 0 + house 2 = 1 + 3

Input:  nums = [1, 2, 3]
Output: 3             # every pair touches, so one house only: the 3
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from the linear House Robber that overcounts on a ring to the two-pass split that drops either the first or the last house, with complexity.

## Follow-up

- Recover the actual set of houses robbed, not just the total. Which of the two passes do you reconstruct from?
- What if the houses form a tree instead of a ring (LeetCode #337, House Robber III)? The "rob it or skip it" pair still works per node.
- With `nums.length` up to 10^5, does anything about the two-slice approach need to change?
