# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `koko_eating_bananas.py`, keep the tests, write it again.

## Key insight

The answer is a number, not a position, and feasibility is monotonic in it: if speed `k` finishes within `h` hours then every faster speed does too, and if `k` fails then every slower speed fails. That makes the range `[1, max(piles)]` look like `[fail, fail, ..., pass, pass]`, so a binary search on the speed finds the first passing value. The check for one candidate is `sum(ceil(pile / k))`, computed as `(pile + k - 1) // k` to stay in integers.

## Complexity

- Time: O(n log m), where n is the number of piles and m is `max(piles)`; each of the log m probes costs a pass over the piles.
- Space: O(1), only the three search variables and the running hour count.

## Mistakes to watch for

- Using `pile // mid` instead of ceiling division. Hours are under-counted, the check passes speeds that are too slow, and `[3,6,7,11], h = 8` returns 3 (which really needs 10 hours) instead of 4.
- Setting `hi = mid - 1` on the feasible branch. `mid` might be the answer, and discarding it means the loop can end on a speed that was never verified; the `lo < hi` / `hi = mid` pairing is what keeps the invariant "hi always works".
- Starting `lo = 0`. Speed 0 divides by zero on the first probe where `mid` lands on it, and it is not a legal speed anyway.
- Searching `[1, sum(piles)]` is correct but wasteful: no speed above `max(piles)` ever helps, since each hour is spent on exactly one pile.

## Related

- `medium/021-search-in-rotated-sorted-array` — binary search over positions instead of over an answer value.
- `medium/038-find-minimum-in-rotated-sorted-array` — the same `lo < hi` / `hi = mid` loop shape, converging on the first element that satisfies a predicate.
- `medium/008-coin-change` — another "minimum something" problem, but without monotonicity, so it needs DP instead of binary search.
- Pattern doc: `../../patterns/binary-search.md`
