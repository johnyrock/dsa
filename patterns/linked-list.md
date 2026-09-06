# Linked List

## When to use

- The problem hands you a `ListNode` chain. There is no random access, so everything is pointer walking.
- Rewiring `next` pointers in place is almost always the intended O(1)-space solution.

## Templates

**Reverse in place:**

```python
prev, curr = None, head
while curr:
    nxt = curr.next       # save before rewiring
    curr.next = prev
    prev, curr = curr, nxt
return prev
```

**Build a result list with a dummy head:**

```python
dummy = ListNode()
tail = dummy
while ...:
    tail.next = chosen_node
    tail = tail.next
return dummy.next
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/007 Reverse Linked List](../easy/007-reverse-linked-list/) | Easy | three pointers, save next first |
| [easy/008 Merge Two Sorted Lists](../easy/008-merge-two-sorted-lists/) | Easy | dummy head, pick the smaller head, attach the remainder |
| [medium/006 Add Two Numbers](../medium/006-add-two-numbers/) | Medium | dummy head, walk both lists with a carry, loop while anything is left |

## Common mistakes

- Rewiring `next` before saving it, which drops the rest of the list.
- Special-casing the first node instead of using a dummy head.
- Forgetting to attach the leftover tail after one list runs out.
- Not handling an empty list or a single node.
- Looping `while l1 and l2` when the loop should run while *either* has nodes (or a carry is pending).
