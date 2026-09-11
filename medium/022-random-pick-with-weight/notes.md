# Notes

## Attempts

- 2026-09-12: Folder generated as reference material, not solved independently. First review should be a from-scratch re-solve: delete `random_pick_with_weight.py`, keep the tests, write it again.

## Key insight

Turn weights into ranges on a number line: prefix sums split `[1, total]` into consecutive chunks, chunk `i` having length `w[i]`. Index `i` "owns" the half-open range `(prefix[i-1], prefix[i]]`. Picking a uniform random integer in `[1, total]` and binary-searching for the first prefix sum `>= target` (`bisect_left`) lands in exactly the chunk whose length — and therefore selection probability — matches `w[i] / total`.

## Complexity

- Time: O(n) once in `__init__` to build prefix sums; O(log n) per `pickIndex` call.
- Space: O(n) for the prefix sums array.

## Mistakes to watch for

- Recomputing prefix sums inside `pickIndex` instead of once in `__init__` — turns each call from O(log n) into O(n), which matters since it's called up to 10^4 times.
- Using `random.randint(0, total - 1)` with `bisect_right` vs `random.randint(1, total)` with `bisect_left` — both are valid schemes, but mixing pieces from each miscounts the boundary and skews probabilities at chunk edges.
- Testing actual randomness with assertions on exact call counts — flaky. Test the deterministic parts (prefix-sum construction, boundary index mapping) instead, as this folder's tests do.

## Related

- Product of Array Except Self (medium) is a different prefix-sum trick — running products instead of running sums used for ranges.
- Merge Intervals / Insert Interval (medium) also model values as ranges on a line, though for a different purpose (overlap merging vs. sampling).
