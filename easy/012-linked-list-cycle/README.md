# 012. Linked List Cycle

**Difficulty:** Easy | **Pattern:** [fast-slow-pointers](../../patterns/fast-slow-pointers.md) ([explained](../../concepts/fast-slow-pointers.html)) | **Source:** LeetCode #141

## Problem

Given the head of a linked list, determine if the list has a cycle: some node's `next` pointer eventually points back to a node earlier in the list.

## Examples

```
Input:  head = [3,2,0,-4], tail connects to node index 1
Output: true

Input:  head = [1,2], tail connects to node index 0
Output: true

Input:  head = [1], no cycle
Output: false
```

## Constraints

- the number of nodes is in `[0, 10^4]`
- must use O(1) extra space (rules out a visited-set)

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the tortoise-and-hare approach.

## Follow-up

- Can you find the node where the cycle begins, not just whether one exists (LeetCode #142)?
