# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete `top_k_frequent_elements.py`, and write it again.

## Key insight

Counting is the easy half (`Counter(nums)`); the real question is how to pick the k largest counts without sorting all of them. A min-heap capped at k entries does it: push every `(count, value)` pair, and whenever the heap grows to k + 1, pop the root, which is the smallest count present and therefore cannot be in the top k. At the end the heap holds exactly the k winners. Because the heap never exceeds k entries, each push and pop is O(log k), not O(log n).

## Complexity

- Time: O(n log k); O(n) to count, then one push (and at most one pop) per distinct value on a heap of size at most k + 1.
- Space: O(n) for the counter in the worst case where every value is distinct; the heap itself is O(k).

## Mistakes to watch for

- Pushing `(num, count)` instead of `(count, num)`. The heap then orders by the values themselves, and on `[1,1,1,2,2,3], k = 2` it evicts `1` (the smallest value, the most frequent one) and returns `{2, 3}`.
- Checking `if len(heap) >= k` before popping. That evicts the moment the heap reaches k, so it can never hold k survivors and the result has k − 1 entries: `[1]` on the running example.
- Popping *before* pushing to keep the size under k. The new pair is never compared against the current root, so a value with a huge count that arrives late is silently dropped.
- Using a max-heap of all n distinct counts and popping k times. It is correct but O(n log n) space-and-time, which is exactly the bound the problem asks you to beat.

## Related

- [easy/018-kth-largest-element-in-a-stream](../../easy/018-kth-largest-element-in-a-stream) is the same size-k min-heap idea, applied to raw values instead of counts.
- [easy/019-last-stone-weight](../../easy/019-last-stone-weight) uses `heapq` the other way around: a max-heap via negation that is drained instead of capped.
- [easy/002-valid-anagram](../../easy/002-valid-anagram) is the `Counter` half of this problem on its own.
- Review the [Heap pattern](../../patterns/heap.md) and its concept page.
