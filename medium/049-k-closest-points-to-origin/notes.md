# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete `k_closest_points_to_origin.py`, and write it again.

## Key insight

The square root never changes which point is closer, so compare `x*x + y*y` directly and stay in integers. Keep a heap of at most `k` points, but make it a *max*-heap on distance (negate the squared distance) so the root is the farthest of the kept points. After each push, if the heap holds `k + 1` entries, pop the root: the point just evicted is farther than `k` others and cannot be in the answer. Whatever remains after the last point is the answer, in heap order.

## Complexity

- Time: O(n log k); one push and at most one pop per point on a heap that never exceeds k + 1 entries.
- Space: O(k) for the heap, plus the output.

## Mistakes to watch for

- Pushing `+(x*x + y*y)` (a min-heap) and popping when the size exceeds `k`. The pop then evicts the *closest* point each time. On `[[3,3],[5,-1],[-2,4]], k = 2` it drops `[3,3]` and returns `[[-2,4],[5,-1]]`, which contains the farthest point.
- Pushing `(x, y, -dist)` with the distance last. The heap then orders by `x` first, so `[5,-1]` (largest x) is treated as the farthest. Put the sort key first in the tuple.
- Comparing with `>=` (`if len(heap) >= k`). The heap is trimmed the moment it reaches `k`, so it can never hold `k` survivors and the result has `k - 1` points.
- Calling `math.sqrt` on every distance. It is not wrong, but it turns exact integer comparisons into floating point ones and buys nothing, because `sqrt` is monotonic.

## Related

- [medium/050-kth-largest-element-in-an-array](../../medium/050-kth-largest-element-in-an-array) is the same size-k heap on plain integers.
- [medium/025-top-k-frequent-elements](../../medium/025-top-k-frequent-elements) is the same trick with `(count, value)` tuples instead of `(-distance, x, y)`.
- [easy/018-kth-largest-element-in-a-stream](../../easy/018-kth-largest-element-in-a-stream) keeps a size-k heap across a stream of `add` calls.
- Review the [Heap pattern](../../patterns/heap.md) and its concept page.
