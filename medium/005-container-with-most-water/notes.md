# Notes

## Attempts

- 2026-09-06: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete `container_with_most_water.py`, keep the tests, write it again.

## Key insight

Start with the widest container, the two ends, and shrink inward. Every inward move loses width, so it only pays off if the height can go up, and the height is capped by the shorter line. Moving the taller line can never help: the shorter line still caps the height and the width is smaller. So always move the shorter line. That one rule visits O(n) pairs and provably never skips the best one.

## Complexity

- Time: O(n). Each iteration moves one pointer inward and they meet after at most n - 1 steps.
- Space: O(1), two indices and a running best.

## Mistakes to watch for

- Moving the taller pointer, or moving both. Only the shorter line can be the bottleneck, so only moving it can raise the ceiling.
- Using the taller height in the area. Water sits at the level of the shorter line.
- Believing the greedy needs a proof you cannot give. The argument is: when `height[left] < height[right]`, every pair `(left, k)` with `k < right` has width smaller than `(left, right)` and height at most `height[left]`, so all of them are already beaten and `left` can be retired.
- Confusing this with Trapping Rain Water. Here you pick two walls; there you sum the water over every column between walls.

## Related

- Trapping Rain Water (LeetCode #42) uses the same shorter-side-moves-inward two-pointer idea with running maxima.
- Two Sum II (LeetCode #167) is the other classic ends-inward pointer sweep on sorted data.
