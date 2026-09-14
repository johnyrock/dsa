# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `partition_equal_subset_sum.py`, keep the tests, write it again.

## Key insight

Two equal halves each sum to `total / 2`, so the problem is really "is there a subset summing to exactly `target = total // 2`?" (the rest of the elements are automatically the other half). Keep a boolean table `dp[s]` = "some subset of the numbers seen so far sums to `s`", seed `dp[0] = True`, and for each number mark `dp[s] = True` wherever `dp[s - num]` already was. The inner loop runs over sums *descending* so that each number is used at most once per subset.

## Complexity

- Time: O(n × target), one pass over the sums for each number. With 200 numbers up to 100, target is at most 10,000: two million cheap steps.
- Space: O(target) for the single-row table.

## Mistakes to watch for

- Iterating the sums ascending (`range(num, target + 1)`). Then `dp[s - num]` may already have been set by this same `num`, so one element gets reused. `[1, 2, 5]` returns `True` (the 1 "used four times" reaches 4) instead of `False`.
- Forgetting `dp[0] = True`. Nothing can ever become reachable, and `[1, 5, 11, 5]` returns `False`.
- Skipping the odd check and using `total / 2` (a float) as the table size or index: `range(5.5)` raises a `TypeError`. Use `total % 2` then `total // 2`.
- Making the inner loop go all the way down to 0: `range(target, -1, -1)` reads `dp[s - num]` with a negative index for `s < num`, which in Python silently wraps to the end of the list and can mark unreachable sums as reachable.

## Related

- [medium/008-coin-change](../008-coin-change/) is the unbounded version of the same table: coins may repeat, so its loop over amounts runs ascending.
- [medium/077-word-break](../077-word-break/) is another boolean reachability table seeded with `dp[0] = True`.
- [easy/024-single-number](../../easy/024-single-number/) — a different way of asking about a hidden subset of an array.
- [patterns/dynamic-programming.md](../../patterns/dynamic-programming.md)
