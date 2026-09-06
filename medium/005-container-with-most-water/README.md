# 005. Container With Most Water

**Difficulty:** Medium | **Pattern:** [two-pointers](../../patterns/two-pointers.md) | **Source:** LeetCode #11

## Problem

You are given an array `height` of `n` non-negative integers. Each value is a vertical line drawn at position `i`, from `(i, 0)` up to `(i, height[i])`.

Pick two lines. Together with the x-axis they form a container. Return the largest amount of water any such container can hold. Water is width times the shorter line, and the container may not be tilted.

## Examples

```
Input:  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49            # lines at index 1 (8) and index 8 (7): width 7, height min(8, 7) = 7

Input:  height = [1, 1]
Output: 1

Input:  height = [4, 3, 2, 1, 4]
Output: 16            # the two 4s at the ends: width 4, height 4
```

## Constraints

- `2 <= height.length <= 10^5`
- `0 <= height[i] <= 10^4`
- the area is `(j - i) * min(height[i], height[j])`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from checking every pair to two pointers that start at the ends and always move the shorter line inward, with the argument for why that never misses the answer.

## Follow-up

- Why is it safe to move the shorter line and never the taller one? What would you lose by moving the taller one?
- Trapping Rain Water (LeetCode #42) has similar pictures but a different question. What changes?
