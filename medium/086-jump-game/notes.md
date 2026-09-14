# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `jump_game.py`, keep the tests, write it again.

## Key insight

The set of reachable indices is always a prefix `0..reach`, because any index below the farthest reachable one is reachable too (take a shorter jump). So one integer, `reach = max(reach, i + nums[i])`, carries the whole state. Sweep left to right; the moment an index `i` sits beyond `reach` nobody can ever land on it, so the answer is `False`. If the sweep finishes, the last index was inside the frontier.

## Complexity

- Time: O(n), one pass with a max per element.
- Space: O(1), a single integer.

## Mistakes to watch for

- Testing `if i >= reach` instead of `i > reach`. At `i = 0` the frontier is 0, so `>=` fires immediately and returns `False` for every input, including `[2,3,1,1,4]`.
- Overwriting instead of taking the max: `reach = i + n`. On `[2,0,0]` the frontier goes 2, then 1, then index 2 looks unreachable and the function returns `False`; the answer is `True` because index 0 could jump straight to index 2.
- Starting the sweep at `range(1, len(nums))` "because index 0 is already reachable". That skips the jump *from* index 0, so `reach` is still 0 when `i = 1` arrives and `[2,3,1,1,4]` returns `False`. Index 0 must be visited to contribute `0 + nums[0]`.
- Simulating one chosen path ("always take the longest jump") instead of tracking the frontier. On `[3,4,0,0,0,1]` the longest jump from index 0 lands on the 0 at index 3 and the simulation reports `False`, while jumping only 1 step to index 1 and then 4 steps reaches the end, so the answer is `True`. The frontier `max(reach, i + n)` counts every path at once, which is why it needs no backtracking.

## Related

- [medium/087-jump-game-ii](../087-jump-game-ii) asks for the minimum number of jumps using the same frontier idea, advanced level by level.
- [medium/088-gas-station](../088-gas-station) is the other single-pass greedy where one running variable decides everything.
- [medium/072-house-robber](../072-house-robber) shows the DP alternative shape: `dp[i]` over indices when the greedy argument is not available.
- Review the [Greedy pattern](../../patterns/greedy.md) and its concept page.
