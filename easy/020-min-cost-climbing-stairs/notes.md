# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

The cheapest way to *stand on* stair `i` is `cost[i]` plus the cheaper of standing on `i - 1` or `i - 2`. That is the Climbing Stairs recurrence with `min` in place of `+`, and it collapses to two rolling variables the same way. Seeding both variables at 0 encodes the free choice of starting on stair 0 or 1: the loop computes `min(0, 0) + cost[0]` and `min(0, cost[0]) + cost[1]`, which is exactly "pay only for the stair you start on". The top is one past the last stair, so the answer is the cheaper of the last two positions.

## Complexity

- Time: O(n), one pass over `cost`.
- Space: O(1), only two integers are alive at any moment.

## Mistakes to watch for

- Returning `current` instead of `min(previous, current)`. The top can be reached from either of the last two stairs; `[10,15,20]` then answers 20 instead of 15.
- Seeding `previous, current = cost[0], cost[1]` and looping from index 2 also works, but seeding `0, cost[0]` does not: it forbids starting on stair 1 and `[10,15,20]` comes back as 25.
- Assigning `previous = current` on its own line before computing the new `current`. The old `previous` is lost and every step pays `current + cost[i]`. Use the tuple assignment so the right side is evaluated first.
- Treating the top as the last index instead of one past it. Then `cost[-1]` is always paid, which is wrong for `[5,7]` (the 7 is never touched).

## Related

- [easy/010-climbing-stairs](../010-climbing-stairs) is the same two-variable loop counting ways instead of minimising cost; the derivation in its notes applies here verbatim with `+` swapped for `min`.
- [medium/008-coin-change](../../medium/008-coin-change) generalises "cheapest way to reach position i from a fixed set of jumps" to arbitrary jump sizes.
- [medium/007-maximum-subarray](../../medium/007-maximum-subarray) is another one-pass DP where the running state is a single best-so-far value.
- Review the [Dynamic Programming pattern](../../patterns/dynamic-programming.md) and its concept page.
