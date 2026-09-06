# Notes

## Attempts

- 2026-09-06: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete `add_two_numbers.py`, keep the tests, write it again.

## Key insight

The reversed storage is a gift: the heads are the ones digits, so walking both lists in step *is* schoolbook addition from right to left. Each column is `carry + digit1 + digit2`, split with `divmod(total, 10)` into the digit to keep and the carry to pass on. A dummy head absorbs the "first node" special case, and looping `while l1 or l2 or carry` handles unequal lengths and the final carry without any extra code.

## Complexity

- Time: O(max(m, n)), one iteration per column, plus at most one extra for the final carry.
- Space: O(max(m, n)) for the result list, which the problem requires. O(1) beyond that.

## Mistakes to watch for

- Looping only `while l1 and l2`, which stops when the shorter list ends and drops the rest of the longer one.
- Forgetting the trailing carry. `[5] + [5]` must give `[0, 1]`, not `[0]`. Putting `carry` in the loop condition handles it; an `if carry` after the loop also works.
- Converting to Python integers and back. It passes here because Python has big ints, but it is O(n) digit conversion each way, it ignores the data structure the question is about, and in most languages it overflows at 100 digits.
- Advancing `l1` or `l2` outside the `if`, which raises on `None`.
- Reversing the lists first. They are already in the order addition needs.

## Related

- Add Two Numbers II (LeetCode #445) stores digits most-significant first; use two stacks or reverse both lists, add, reverse the result.
- Merge Two Sorted Lists (easy/008) is the same dummy-head, walk-two-lists-in-step shape.
- Plus One (LeetCode #66) is the array version of a carry ripple.
