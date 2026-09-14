# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

The rule only ever touches the two heaviest stones, so a max-heap is the exact structure: pop twice, push the difference if it is nonzero, repeat while at least two stones remain. `heapq` is a min-heap, so every weight is stored negated (`-stone`) and un-negated on the way out; the largest weight is then the smallest stored value. The loop ends with zero or one stones, and `-heap[0] if heap else 0` handles both.

## Complexity

- Time: O(n log n); heapify is O(n), and each of at most n - 1 smashes does two pops and at most one push at O(log n).
- Space: O(n) for the heap.

## Mistakes to watch for

- Sign slip on the re-insert. `first` is popped first, so it is the heavier stone; the real difference is `first - second`, and it must go back in negated, i.e. `heappush(heap, second - first)`. Pushing `first - second` inserts a positive number into a heap of negatives, which sorts as the *lightest* stone and never gets smashed. Check with `[8,7]`: the answer must be `1`.
- Pushing the difference when it is 0. `[3,3]` then leaves a phantom stone of weight 0 in the heap; harmless for the final answer here but wrong in spirit and breaks a "count remaining stones" variant.
- Returning `heap[0]` without re-negating, giving `-1` instead of `1`.
- Sorting once and taking the two largest each round. The difference must be re-inserted in order; a plain list needs a re-sort or `insort` every round, which is what the heap is avoiding.

## Related

- [easy/018-kth-largest-element-in-a-stream](../018-kth-largest-element-in-a-stream) is the companion heap problem; it keeps a min-heap of fixed size instead of draining a max-heap.
- [medium/008-coin-change](../../medium/008-coin-change) is where Last Stone Weight II ends up: the "split into two piles with minimal difference" follow-up is a knapsack DP.
- [medium/009-merge-intervals](../../medium/009-merge-intervals) is another "process the largest/earliest first" problem, done with a sort instead of a heap because nothing is re-inserted.
- Review the [Heap pattern](../../patterns/heap.md) and its concept page.
