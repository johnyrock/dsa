# Fast & Slow Pointers

## When to use

- Detecting a cycle in a linked list (or any sequence defined by repeated application of a function) without extra memory.
- Finding the middle of a linked list in one pass.
- Any problem where two pointers moving at different speeds through the same structure reveal a repeating or midpoint property.

## Templates

**Cycle detection (Floyd's tortoise and hare):**

```python
slow = fast = head
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow is fast:
        return True
return False
```

**Middle of a linked list:**

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow  # middle node (second middle if even length)
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/012 Linked List Cycle](../easy/012-linked-list-cycle/) | Easy | slow steps by 1, fast by 2; they meet only if a cycle exists |

## Common mistakes

- Checking only `fast is not None` and then dereferencing `fast.next.next`, which crashes when `fast.next` is `None`. Both halves of the guard are required.
- Comparing nodes with `==` instead of `is` — relies on identity, not value equality.
- Starting `fast` one step ahead "for safety" — unnecessary, and complicates the self-loop edge case (a single node pointing to itself).
