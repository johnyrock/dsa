# 040. Reorder List

**Difficulty:** Medium | **Pattern:** [linked-list](../../patterns/linked-list.md) ([explained](../../concepts/linked-list.html)) | **Source:** LeetCode #143

## Problem

You are given the head of a singly linked list `L0 -> L1 -> ... -> Ln-1 -> Ln`. Reorder it in place so that it reads `L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...`, alternating one node from the front with one node from the back.

Only the `next` pointers may be changed; the node values must stay where they are. The function returns nothing and the list is modified in place.

## Examples

```
Input:  head = [1,2,3,4,5]
Output: [1,5,2,4,3]       # front 1, back 5, front 2, back 4, the middle 3 is left over

Input:  head = [1,2,3,4]
Output: [1,4,2,3]         # even length: the halves [1,2] and [3,4] interleave with nothing left over

Input:  head = [1,2,3]
Output: [1,3,2]           # the smallest list where anything actually moves
```

## Constraints

- the number of nodes in the list is in the range `[1, 5 * 10^4]`
- `1 <= Node.val <= 1000`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from copying the nodes into an array to the three-phase find-middle / reverse / merge rewiring, with complexity.

## Follow-up

- Palindrome Linked List (LeetCode #234) uses the same find-middle-and-reverse machinery. What does the third phase become, and what should you do to the list before returning?
- Reorder the list into `L0 -> Ln -> L2 -> Ln-2 -> ...` — skipping every other front node. Which phase changes, and does the merge loop still terminate on `second`?
- The problem asks for O(1) extra space. If that constraint were dropped, what is the simplest correct solution, and is it actually faster in practice?
