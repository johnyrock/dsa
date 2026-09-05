# 008. Merge Two Sorted Lists

**Difficulty:** Easy | **Pattern:** [linked-list](../../patterns/linked-list.md) | **Source:** LeetCode #21

## Problem

You are given the heads of two singly linked lists, `list1` and `list2`, each already sorted in non-decreasing order.

Splice the two lists together into one sorted list by relinking the existing nodes, and return the head of the merged list.

## Examples

```
Input:  list1 = [1, 2, 4], list2 = [1, 3, 4]
Output: [1, 1, 2, 3, 4, 4]

Input:  list1 = [], list2 = []
Output: []            # nothing to merge

Input:  list1 = [], list2 = [0]
Output: [0]           # one empty list, return the other unchanged
```

## Constraints

- `0 <= list1.length, list2.length <= 50`
- `-100 <= Node.val <= 100`
- both lists are already sorted in non-decreasing order
- either list may be empty

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from collect-sort-rebuild to the one-pass dummy head merge, with complexity.

## Follow-up

- Collecting the values, sorting, and rebuilding is O((n + m) log(n + m)). Can you do it in one pass with O(1) extra space?
- What changes if you have to merge k sorted lists instead of two? (LeetCode #23)
