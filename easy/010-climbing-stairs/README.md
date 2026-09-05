# 010. Climbing Stairs

**Difficulty:** Easy | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) | **Source:** LeetCode #70

## Problem

You are climbing a staircase with `n` steps. Each move takes you either 1 step or 2 steps up.

Return how many distinct sequences of moves reach the top.

## Examples

```
Input:  n = 2
Output: 2             # 1+1, or 2

Input:  n = 3
Output: 3             # 1+1+1, 1+2, 2+1

Input:  n = 5
Output: 8             # the counts run 1, 2, 3, 5, 8
```

## Constraints

- `1 <= n <= 45`
- each move is exactly 1 or 2 steps
- two sequences are different if the order of moves differs

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from the exponential recursion to the two-variable bottom-up loop, with complexity.

## Follow-up

- The plain recursion is O(2^n). Can you get it to O(n) time and O(1) space?
- What changes if each move can be 1, 2, or 3 steps?
