# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `merge_triplets_to_form_target_triplet.py`, keep the tests, write it again.

## Key insight

Merging is an element-wise `max`, so values only ever go up. A triplet with any value above the target in that position can never be part of the answer: including it would push that position past the target for good. Every other triplet is harmless to include, so the greedy move is to merge *all* of them and check the result. Merging every safe triplet equals `target` exactly when each of the three positions is hit by at least one safe triplet, which is what the `found` set of matched positions records.

## Complexity

- Time: O(n), one pass over the triplets with constant work (three comparisons, three equality checks) each.
- Space: O(1), the `found` set holds at most three indices.

## Mistakes to watch for

- Recording a matched position *before* checking the whole triplet is safe. `[1, 8, 4]` against target `[2, 7, 5]` matches nothing, but `[2, 8, 4]` would set `found = {0}` even though its 8 makes it unusable; on `[[2, 8, 4], [1, 7, 5]]` that returns `True` when the real answer is `False`.
- Checking `triplet[i] < target[i]` instead of `<=`. A triplet that equals the target in some position is exactly the one you need, and a strict test throws it out; `[[2, 7, 5]]` with target `[2, 7, 5]` would return `False`.
- Trying to find a single triplet equal to the target. The answer usually needs two or three triplets combined; `[[2, 5, 3], [1, 7, 5]]` has no triplet equal to `[2, 7, 5]` but the answer is `True`.
- Counting matches instead of collecting positions. `[[2, 1, 1], [2, 1, 1], [2, 1, 1]]` against `[2, 7, 5]` produces three matches, all of position 0, and a counter reaching 3 would wrongly say `True`.

## Related

- [medium/035-car-fleet](../../medium/035-car-fleet/) is another greedy pass where one comparison per element settles whether it can be absorbed.
- [medium/051-task-scheduler](../../medium/051-task-scheduler/) is greedy too, choosing the most frequent task first.
- Pattern doc: [greedy](../../patterns/greedy.md).
