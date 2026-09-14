# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `detect_squares.py`, keep the tests, write it again.

## Key insight

An axis-aligned square is fixed by one diagonal: once the query point `(px, py)` and a stored point `(x, y)` with `|x - px| == |y - py| != 0` are chosen as opposite corners, the other two corners are forced to be `(x, py)` and `(px, y)`. So `count` loops over the stored points as diagonal candidates and, for each valid one, multiplies the stored copies of the three non-query corners. A `defaultdict(int)` keyed by `(x, y)` makes the missing-corner case read as 0 and multiply the term away.

## Complexity

- Time: `add` is O(1); `count` is O(k) where k is the number of distinct stored points (at most 3000).
- Space: O(k) for the counter.

## Mistakes to watch for

- Storing points in a `set` instead of a counter. After the second `add([11, 2])` the running example's final `count([11, 10])` returns 1 instead of 2, because the two copies of `(11, 2)` collapse to one.
- Forgetting `x == px` in the skip condition. A stored copy of the query point itself passes `abs(0) == abs(0)` and adds `n * n * n` "squares" of side 0: with `(11, 10)` added once, `count([11, 10])` on the example returns 3 instead of 2.
- Checking only `x != px and y != py` and not that the offsets are equal. That counts rectangles: `add([0, 0])`, `add([1, 2])`, `add([0, 2])`, `count([1, 0])` returns 1 instead of 0.
- Using `self.count_at.get((x, py))` and multiplying without a default, or a plain `dict` with `[]` access, which raises `KeyError` on the first missing corner instead of contributing 0.

## Related

- [easy/001-two-sum](../../easy/001-two-sum/) — the same "look up the partner you need" move with a hash map.
- [medium/028-longest-consecutive-sequence](../../medium/028-longest-consecutive-sequence/) — O(1) membership checks turning a scan into linear work.
- [medium/031-min-stack](../../medium/031-min-stack/) — another design-class problem where every operation must stay cheap.
- Pattern doc: [patterns/hash-map.md](../../patterns/hash-map.md)
