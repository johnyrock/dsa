# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `house_robber.py`, keep the tests, write it again.

## Key insight

For each house the decision is binary: rob it and add its money to the best total from two houses back, or leave it and keep the best total from one house back. `best[i] = max(best[i-1], best[i-2] + nums[i])`. Only the previous two bests are ever read, so the table collapses into two rolling variables, `skip` (two back) and `take` (one back), updated with a single tuple assignment. It is the Climbing Stairs shape with `max` in place of `+`.

## Complexity

- Time: O(n), one pass over `nums`.
- Space: O(1), two integers.

## Mistakes to watch for

- Splitting the tuple assignment into `skip = take` then `take = max(take, skip + money)`. The second line now reads the *new* `skip`, so it computes `take + money` and simply sums every house: `22` instead of `12` on `[2,7,9,3,1]`.
- Forcing alternation with `take = skip + money` instead of `max(take, skip + money)`. It happens to give `12` on the running example but returns `6` on `[4,1,1,4,1]`, where the answer is `8` (houses 0 and 3).
- Returning `skip` instead of `take`. That is the best total *excluding the last house*: `11` instead of `12` on the running example.
- Seeding with `take = nums[0]` and then looping from index 0 anyway lets house 0 pair with house 1 on inputs like `[2, 1]` (returns 3, not 2).

## Related

- `easy/010-climbing-stairs` — the same two-variable recurrence with `+` instead of `max`.
- `easy/020-min-cost-climbing-stairs` — a per-step cost version of the same table.
- `medium/012-longest-palindromic-substring` — another dynamic-programming entry in this repo.
- `patterns/dynamic-programming.md` — the pattern doc.
