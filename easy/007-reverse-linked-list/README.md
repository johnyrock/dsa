# 007. Reverse Linked List

**Difficulty:** Easy | **Pattern:** [linked-list](../../patterns/linked-list.md) | **Source:** LeetCode #206

## Problem

Given the head of a singly linked list, reverse the list and return the head of the reversed list.

Reverse it in place by rewiring the existing nodes, not by building a new list out of the values.

## Examples

```
Input:  head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Input:  head = [1, 2]
Output: [2, 1]

Input:  head = []
Output: []              # empty list, nothing to reverse
```

## Constraints

- `0 <= number of nodes <= 5000`
- `-5000 <= Node.val <= 5000`
- the list is singly linked and contains no cycle

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from copying the values out to the in-place three-pointer rewiring, with complexity.

## Follow-up

- The iterative version uses O(1) extra space. Can you write it recursively, and what does the recursion cost you?
