# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `time_based_key_value_store.py`, keep the tests, write it again.

## Key insight

Because timestamps for one key arrive strictly increasing, appending to a per-key list keeps that list sorted for free, so `set` is O(1). `get` then becomes "find the last timestamp `<= t` in a sorted list", which is the rightmost-boundary binary search: `lo, hi = 0, len(times)`, move `lo = mid + 1` while `times[mid] <= t`, else `hi = mid`. When the loop ends `lo` is the number of timestamps `<= t` (the same thing `bisect.bisect_right` returns), so the answer is `values[lo - 1]`, or `""` when `lo == 0`.

## Complexity

- Time: `set` O(1) amortized (an append); `get` O(log k) where k is the number of writes to that key.
- Space: O(n) for n total writes, since every value is kept.

## Mistakes to watch for

- Using `times[mid] < timestamp` instead of `<=`. That computes the `bisect_left` position, so an exact hit is treated as "too new": `get("foo", 4)` on the running example returns `"bar"` instead of `"bar2"`.
- Returning `values[lo]` instead of `values[lo - 1]`. `lo` is the insertion point, one past the answer: `get("foo", 5)` returns `"bar3"` and `get("foo", 9)` raises `IndexError`.
- Forgetting the `lo == 0` guard. `values[-1]` is a valid Python index, so `get("foo", 0)` silently returns the *newest* value `"bar3"` instead of `""`.
- Setting `hi = len(times) - 1` with the `lo < hi` / `hi = mid` loop. If every timestamp qualifies the search can never advance `lo` past the last index, so `get("foo", 9)` returns `"bar2"` instead of `"bar3"`.

## Related

- `medium/011-lru-cache` — the other "design a store" problem here; a dict keyed by `key` is the front door in both.
- `medium/038-find-minimum-in-rotated-sorted-array` — the same `lo < hi` boundary-search loop, finding the first index where a predicate flips.
- `medium/022-random-pick-with-weight` — binary search over a prefix-sum array, another "rightmost position <= target" search.
- Pattern doc: `../../patterns/binary-search.md`
