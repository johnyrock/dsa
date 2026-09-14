# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `car_fleet.py`, keep the tests, write it again.

## Key insight

Whether a car joins the fleet ahead of it depends only on arrival times: compute `time = (target - pos) / spd` for every car as if the road were empty, sort the cars from closest-to-target to farthest, and walk them front to back. A car that would arrive *no later* than the fleet ahead of it catches that fleet before the target and merges (the fleet keeps the slower leader's time); a car that would arrive later never catches up and starts a new fleet. A stack of fleet times, compared only against its top, counts the fleets; it is never popped, because a merged car adopts the time already on top.

## Complexity

- Time: O(n log n) for the sort; the pass afterwards is O(n).
- Space: O(n) for the sorted pairs and the stack of fleet times.

## Mistakes to watch for

- Using `>=` instead of `>` when deciding a new fleet. Cars that arrive at exactly the same time meet at the target and count as one fleet; with `>=` the running example returns 4 instead of 3 because the cars at 10 and 8 (both 1.0h) are counted separately.
- Sorting ascending (farthest car first). The stack then compares each car against the one *behind* it, and the running example collapses to 1 fleet. Processing must go front to back so each car is only ever measured against cars it could actually be blocked by.
- Using integer division `//` for the time. `(12 - 8) // 4 = 1` and `(12 - 10) // 2 = 1` happen to agree here, but `(10 - 6) // 3 = 1` rounds the car at 6 down to the same time as the car at 8 (`(10 - 8) // 2 = 1`), merging two cars that never meet: 1 instead of 2 for `target = 10, position = [6, 8], speed = [3, 2]`.
- Sorting by speed, or forgetting to pair position with speed before sorting, so the speeds no longer line up with their cars.

## Related

- [medium/034-daily-temperatures](../034-daily-temperatures) is the same monotonic-stack shape where a new element resolves against the top.
- [medium/009-merge-intervals](../009-merge-intervals) also sorts first and then merges each item into the group on top or starts a new one.
- [easy/021-meeting-rooms](../../easy/021-meeting-rooms) is the simplest "sort, then compare each with its predecessor" problem.
- Review the [Stack pattern](../../patterns/stack.md) and its concept page.
