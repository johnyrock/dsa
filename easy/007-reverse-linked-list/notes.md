# Notes

## Attempts

- 2026-09-05: Folder generated as reference material, not solved independently. The solution, the annotated version and the walkthrough were written out rather than worked out, so there is no real attempt behind them yet. First review should be a from-scratch re-solve: delete `reverse_linked_list.py`, keep the tests, write it again.

## Key insight

Reversing the list is just flipping every arrow, one node at a time. The only thing that makes it tricky is that `curr.next = prev` destroys the way forward, so you have to save `curr.next` into a temporary before you overwrite it. Three pointers — `prev`, `curr`, `next_node` — are enough, and no extra list is needed.

## Complexity

- Time: O(n), each node is visited and rewired exactly once.
- Space: O(1), only three pointers regardless of list length.

## Building the test list

The tests need a helper that turns `[1, 2, 3]` into a chain of nodes. Two ways work:

- **Front to back (used here).** Keep a `dummy` node in front and a `tail` pointer at the last node added, then `tail.next = ListNode(v); tail = tail.next` for every value, and return `dummy.next`. The dummy exists only so the first value is not a special case — without it you need an `if head is None` branch. Same shape as the splicing code in Merge Two Sorted Lists and Add Two Numbers.
- **Back to front.** `for v in reversed(values): head = ListNode(v, head)`. Shorter, no tail pointer, because a node can be created already pointing at the current head — but that only works if the tail is built first, hence the `reversed()`. Correct, just harder to read at a glance.

Both are O(n). Prefer the first; see [concepts/linked-list.html](../../concepts/linked-list.html) for a traced comparison.

## Mistakes to watch for

- Saving `next_node = curr.next` *after* the rewiring instead of before. By then `curr.next` is `prev`, so you walk backwards into the part you already reversed and lose the tail.
- Returning `head` at the end. `head` is the old head, which is now the tail. The new head is `prev`.
- Starting `prev` at `head` instead of `None`. The old head must end up pointing at `None`, or the reversed list has a cycle.
- Empty list: `head is None` means the loop never runs and `prev` is still `None`, which is the right answer. Single node: one iteration sets `node.next = None` and returns the same node. Neither needs a special case.
- The recursive version reverses the tail first and then does `head.next.next = head; head.next = None`. It is O(n) time but O(n) stack space, and with 5000 nodes it is close to Python's recursion limit. Prefer the iterative one in an interview and mention the recursive one as an aside.

## Related

- Reverse Linked List II (medium) reverses only a sublist, using the same three-pointer flip with a saved boundary node.
- Palindrome Linked List uses this to reverse the second half after finding the middle with slow/fast pointers.
- Reverse Nodes in k-Group (hard) is this loop run in fixed-size chunks.
