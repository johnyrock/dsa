# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

Keep only the `k` largest values seen so far in a min-heap. The heap's root is the smallest of those `k`, which is exactly the k-th largest overall. On `add`, push the new value and, if the heap has grown to `k + 1`, pop once: the pop always removes the smallest, so whatever fell out was never in the top `k`. The constructor heapifies `nums` and pops down to size `k` the same way.

## Complexity

- Time: O(n log n) to build (heapify is O(n), then up to n - k pops at O(log n) each); O(log k) per `add`.
- Space: O(k), the heap never holds more than `k` values.

## Mistakes to watch for

- Using a max-heap (negating values). The root is then the largest, not the k-th largest, and you cannot evict cheaply.
- Popping before pushing (`if len == k: pop; push`). That throws away the current minimum even when the new value is smaller than it, and the answer creeps upward.
- Assuming `nums` has at least `k` elements. `nums` may be empty; the constructor loop `while len(heap) > k` simply does nothing and `add` fills the heap up to `k` before evicting anything.
- Returning `heap[0]` after a push without the size check when `len(heap) == k` already. The heap becomes `k + 1` long and the root is the (k+1)-th largest.

## Related

- [easy/019-last-stone-weight](../019-last-stone-weight) is the other introductory heap problem, using the max-heap-by-negation trick this one deliberately avoids.
- [medium/017-kth-smallest-element-in-a-bst](../../medium/017-kth-smallest-element-in-a-bst) is the same "k-th" question answered with an in-order walk when the data is already a BST.
- [medium/022-random-pick-with-weight](../../medium/022-random-pick-with-weight) is another "design a class, preprocess in `__init__`, answer queries fast" problem.
- Review the [Heap pattern](../../patterns/heap.md) and its concept page.
