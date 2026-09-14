# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `house_robber_ii.py`, keep the tests, write it again.

## Key insight

On a circle the only new constraint is that house 0 and house n-1 cannot both be robbed. So either house 0 is left alone (rob the line `nums[1:]`) or house n-1 is left alone (rob the line `nums[:-1]`); every valid plan falls into at least one of those two cases. Each line is the ordinary House Robber with two rolling variables, `skip` and `take`, and the answer is the larger of the two passes. A single house is the one input where both slices are empty, so it is returned directly.

## Complexity

- Time: O(n), two linear passes over n - 1 houses each.
- Space: O(1) beyond the two slices (which can be avoided by passing index bounds instead of slicing).

## Mistakes to watch for

- Running the linear robber on the whole array. On `[2, 3, 2]` it takes houses 0 and 2 for 4, but they are neighbours on the ring; the answer is 3.
- Forgetting the single-house case. `nums[1:]` and `nums[:-1]` are both empty for `[1]`, so `max(0, 0) = 0` comes back instead of 1.
- Writing the update as two statements, `skip = take` then `take = max(take, skip + money)`: the second line now reads the *new* skip, which equals take, and the robber ends up taking adjacent houses (`[2, 3, 2]` gives 7).
- Slicing `nums[1:-1]` to "drop both ends" and returning that single pass. That forbids both end houses at once, which is stricter than the problem; `[200, 3, 140, 20, 10]` would give 160 instead of 340.

## Related

- [House Robber](../072-house-robber) (medium/072) is the linear version this solution calls twice.
- [Climbing Stairs](../../easy/010-climbing-stairs) (easy/010) is the same two-variable rolling window with a sum instead of a max.
- [Min Cost Climbing Stairs](../../easy/020-min-cost-climbing-stairs) (easy/020) is another "keep the last two answers" table.
- Pattern doc: [dynamic-programming](../../patterns/dynamic-programming.md).
