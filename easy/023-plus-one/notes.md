# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

Adding one only produces a carry when the current digit is `9`. Scanning from the last digit leftward, the first digit below `9` absorbs the increment and nothing to its left changes, so the function can return immediately. Every `9` passed along the way becomes `0`. If the loop runs off the left end, every digit was `9` and the answer is a `1` followed by all those zeros.

## Complexity

- Time: O(n) in the worst case (all nines); O(1) when the last digit is below 9.
- Space: O(1) extra, except the all-nines case, which builds a new list of length `n + 1`.

## Mistakes to watch for

- Iterating with `range(len(digits), 0, -1)` or `range(len(digits) - 1, 0, -1)`. The first indexes past the end; the second skips index 0, so `[9]` never gets zeroed and the fallback returns `[1, 9]`.
- Testing `digits[index] == 9` and zeroing, but forgetting the `else` branch that increments and returns. The loop then keeps walking left after the carry is already absorbed.
- Returning `digits` after the loop instead of `[1] + digits`. For `[9, 9]` that returns `[0, 0]`.
- Prepending with `digits.insert(0, 1)` works but is O(n) anyway; `[1] + digits` is clearer and the same cost.

## Related

- [medium/006-add-two-numbers](../../medium/006-add-two-numbers/) is the general carry propagation over two linked lists of digits.
- [easy/007-reverse-linked-list](../../easy/007-reverse-linked-list/) matters for the same reason: digit arrays and lists stored most-significant-first have to be walked from the far end.
- Add Binary (easy, LeetCode #67) is the same right-to-left carry with base 2 strings.
- Pattern doc: [two-pointers](../../patterns/two-pointers.md).
