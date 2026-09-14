# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete `kth_largest_element_in_an_array.py`, and write it again.

## Key insight

Keep a min-heap of at most `k` values. Push every number; whenever the heap holds `k + 1`, pop the root, which is the smallest of them and therefore cannot be among the `k` largest. After the last number the heap holds exactly the `k` largest, and the root of a min-heap is the smallest of those: the `k`th largest. No negation is needed here, because the value we want to evict (the smallest survivor) is already what a min-heap puts at the root.

## Complexity

- Time: O(n log k); one push and at most one pop per element, on a heap that never exceeds k + 1 entries. Sorting is O(n log n); quickselect is O(n) average but O(n²) worst case.
- Space: O(k) for the heap.

## Mistakes to watch for

- Negating the values out of habit from max-heap problems. A max-heap capped at `k` evicts the *largest* each time, and on `[3,2,1,5,6,4], k = 2` returns 2 (the 2nd smallest) instead of 5.
- Checking `if len(heap) >= k` before popping. The heap is trimmed the moment it reaches `k`, so it can never hold `k` values; on the running example it ends as `[6]` and returns 6, the 1st largest.
- Popping before pushing to keep the size under `k`. The newcomer is never compared against the current root, so `6` arriving late could evict a survivor without being checked itself.
- Returning `heap[-1]` or `heapq.heappop(heap)` repeatedly. `heap[-1]` is not the maximum of a heap, just the last leaf; only `heap[0]` has a guaranteed meaning.

## Related

- [easy/018-kth-largest-element-in-a-stream](../../easy/018-kth-largest-element-in-a-stream) is this exact heap kept alive across `add` calls.
- [medium/025-top-k-frequent-elements](../../medium/025-top-k-frequent-elements) applies the same size-k min-heap to `(count, value)` pairs.
- [medium/049-k-closest-points-to-origin](../../medium/049-k-closest-points-to-origin) is the mirror image: a max-heap capped at k to keep the smallest distances.
- Review the [Heap pattern](../../patterns/heap.md) and its concept page.
