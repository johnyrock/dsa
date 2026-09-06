# 006. Add Two Numbers

**Difficulty:** Medium | **Pattern:** [linked-list](../../patterns/linked-list.md) | **Source:** LeetCode #2

## Problem

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, one digit per node, so the head holds the ones digit.

Add the two numbers and return the sum as a linked list in the same reversed format.

Neither number has leading zeros, except the number 0 itself.

## Examples

```
Input:  l1 = [2, 4, 3], l2 = [5, 6, 4]
Output: [7, 0, 8]           # 342 + 465 = 807

Input:  l1 = [0], l2 = [0]
Output: [0]

Input:  l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
Output: [8, 9, 9, 9, 0, 0, 0, 1]   # 9999999 + 9999 = 10009998
```

## Constraints

- `1 <= number of nodes in each list <= 100`
- `0 <= Node.val <= 9`
- the lists may have different lengths, and the sum may be one digit longer than either input

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from converting to integers and back to a single pass of schoolbook addition with a carry, with complexity.

## Follow-up

- What changes if the digits were stored most-significant first? (LeetCode #445)
- Why does the loop condition include the carry, and what breaks if it does not?
