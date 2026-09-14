# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `jump_game_ii.py`, keep the tests, write it again.

## Key insight

Think of it as breadth-first search where level `k` is the set of indices reachable with exactly `k` jumps. Because the reachable set is always a contiguous window, a level is just an interval `[start, end]`, and the next level is `[end + 1, farthest]` where `farthest = max(i + nums[i])` over the current window. So sweep `i` left to right, keep `farthest` up to date, and every time `i` hits `end` you have exhausted a level: count one jump and set `end = farthest`. The loop stops at `len(nums) - 2` because standing on the last index needs no further jump.

## Complexity

- Time: O(n), one pass with a max and a comparison per index.
- Space: O(1), three integers.

## Mistakes to watch for

- Looping over `range(len(nums))` instead of `range(len(nums) - 1)`. When `i` reaches the last index it also equals `end`, so a phantom jump is counted: `[2,3,1,1,4]` returns 3 instead of 2, and `[0]` returns 1 instead of 0.
- Updating `end = farthest` on every iteration instead of only when `i == end`. Then `end` runs ahead of `i` from the very first iteration, `i == end` is never true again, and `jumps` stays 0: `[2,3,1,1,4]` returns 0 instead of 2.
- Setting `end = i + nums[i]` when the window closes instead of `end = farthest`. That launches from the *last* index of the window rather than the best one; on `[2,3,1,1,4]` the window `[1, 2]` closes at index 2, which only reaches 3, so a third jump is needed: 3 instead of 2.
- Greedy on the jump itself ("always jump as far as possible") is a different, wrong algorithm: on `[2,3,1,1,4]` it goes 0 → 2 → 3 → 4, three jumps. The correct greedy is on the *window*, choosing the launch point with the best `i + nums[i]`.

## Related

- [medium/086-jump-game](../086-jump-game) is the yes/no version, where the same `farthest` frontier answers reachability in one pass.
- [medium/088-gas-station](../088-gas-station) is another single sweep where a running variable resets at well-defined points.
- [medium/008-coin-change](../008-coin-change) is the shortest-path-by-levels idea done with DP when no window structure exists.
- Review the [Greedy pattern](../../patterns/greedy.md) and its concept page.
