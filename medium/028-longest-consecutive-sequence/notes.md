# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete `longest_consecutive_sequence.py`, and write it again.

## Key insight

Put the values in a set so `x in seen` is O(1). A value `num` is the *start* of a run exactly when `num - 1` is not in the set. Only from those starts, count upward with `while num + length in seen` until the run breaks. Every value is visited by at most one such walk (the one from its run's start), so the total walking is O(n) even though there is a `while` inside a `for`. Skipping non-starts is what makes it linear; without that check the same runs are re-walked from every member.

## Complexity

- Time: O(n); building the set is O(n), and each value is stepped over by exactly one upward walk.
- Space: O(n) for the set.

## Mistakes to watch for

- Dropping the `if num - 1 in seen: continue` guard. The output is still correct, but each run is walked from every member: on `[100,4,200,1,3,2]` that is 12 membership steps instead of 6, and on a single run of n values it is O(n²), which times out at 10^5.
- Checking the wrong side, `if num + 1 in seen: continue`. Now only the *tops* of runs survive, and walking upward from a top finds nothing: the running example returns 1 instead of 4.
- Inverting the guard to `if num - 1 not in seen: continue`. The starts are skipped and only mid-run values walk, so the run 1–4 is measured from 2 at best: 3 instead of 4 on the running example.
- Initialising `best = 1` "because a single value is a run". That returns 1 for the empty array, where the answer is 0.
- Iterating `nums` instead of `seen`. With duplicates, each copy of a run's start walks the whole run again, which brings back the O(n²) worst case.

## Related

- [easy/003-contains-duplicate](../../easy/003-contains-duplicate) is the basic "put it in a set, ask if it is there" move this problem builds on.
- [easy/001-two-sum](../../easy/001-two-sum) uses the same O(1) lookup to avoid a nested loop.
- [easy/028-missing-number](../../easy/028-missing-number) is also about which integers of a range are present, solved arithmetically instead of with a set.
- Review the [Hash Set pattern](../../patterns/hash-set.md) and its concept page.
