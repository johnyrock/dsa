# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `min_stack.py`, keep the tests, write it again.

## Key insight

The minimum of a stack only changes at two moments: when a new value at or below the current minimum is pushed, and when that value is later popped. So keep a second stack, `min_stack`, that records every value that was a minimum at push time. Its top is always the current minimum, because everything above the previous minimum in the main stack is popped before it is. `push` appends to `min_stack` when `val <= min_stack[-1]`; `pop` pops `min_stack` when the value leaving equals its top.

## Complexity

- Time: O(1) for `push`, `pop`, `top`, and `get_min`; each is a constant number of list operations at the end of a list.
- Space: O(n) worst case, when values are pushed in non-increasing order and every one lands on `min_stack`.

## Mistakes to watch for

- Only popping the main stack. `pop` must also pop `min_stack` when the departing value equals its top. Otherwise, on the running example, `get_min` returns `-3` after `-3` has been popped, instead of `-2`.
- Using `<` instead of `<=` in `push`. With `push(1), push(1), pop()`, only the first `1` reaches `min_stack`; the pop then removes it, and `get_min` on the remaining `1` reads an empty list and raises `IndexError`.
- Recomputing the minimum with `min(self.stack)` in `get_min`. Correct, but O(n) per call, which fails the problem's stated requirement of O(1) for every operation.
- Storing the minimum in a single variable. After popping the current minimum there is no way to recover the previous one; that is precisely what the second stack remembers.

## Related

- `easy/004-valid-parentheses` is the plain stack pattern this builds on.
- `medium/011-lru-cache` is another design problem where a second structure keeps a derived fact (recency there, minimum here) available in O(1).
- `easy/018-kth-largest-element-in-a-stream` also maintains an order statistic across a stream of operations, using a heap instead.
- Pattern doc: `patterns/stack.md`
