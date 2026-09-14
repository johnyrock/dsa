# 041. Remove Nth Node From End of List

**Difficulty:** Medium | **Pattern:** [two-pointers](../../patterns/two-pointers.md) ([explained](../../concepts/two-pointers.html)) | **Source:** LeetCode #19

## Problem

Given the `head` of a singly linked list and an integer `n`, remove the `n`-th node counting from the end of the list and return the head of the modified list.

The list is not doubly linked and you do not know its length up front, so "n-th from the end" has to be located from the front.

## Examples

```
Input:  head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]        # the 2nd from the end is 4; 3.next is rewired to 5

Input:  head = [1], n = 1
Output: []               # removing the only node leaves an empty list

Input:  head = [1,2], n = 2
Output: [2]              # the 2nd from the end is the head itself
```

## Constraints

- the number of nodes in the list is `sz`
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the two-pass length count, the gap-of-n two-pointer walk, the dummy node, pitfalls, and complexity.

## Follow-up

- Could you do this in one pass? (The two-pointer version already does; the two-pass version counts first.)
- How would you remove the `n`-th node from the *start* with the same dummy-node trick, and why is that version simpler?
- If `n` could be larger than the list length, what should the function return, and where would you detect it?
