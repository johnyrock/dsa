# Heap

## When to use

- You repeatedly need the smallest or largest remaining value.
- The input arrives as a stream and you only need the best `k` values seen so far.
- Sorting once is not enough because a new value is inserted after each decision.

## Templates

**Keep the k largest values with a min-heap:**

```python
import heapq

heap = []
for value in values:
    heapq.heappush(heap, value)
    if len(heap) > k:
        heapq.heappop(heap)
answer = heap[0]
```

**Use a max-heap with negated values in Python:**

```python
heap = [-value for value in values]
heapq.heapify(heap)
largest = -heapq.heappop(heap)
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/018 Kth Largest Element in a Stream](../easy/018-kth-largest-element-in-a-stream/) | Easy | min-heap of exactly k kept values |
| [easy/019 Last Stone Weight](../easy/019-last-stone-weight/) | Easy | negated max-heap exposes the two heaviest stones |
| [medium/025 Top K Frequent Elements](../medium/025-top-k-frequent-elements/) | Medium | Counting is the easy half (`Counter(nums)`); the real question is how to pick the k… |
| [medium/049 K Closest Points to Origin](../medium/049-k-closest-points-to-origin/) | Medium | The square root never changes which point is closer, so compare `x*x + y*y` directly… |
| [medium/050 Kth Largest Element in an Array](../medium/050-kth-largest-element-in-an-array/) | Medium | Keep a min-heap of at most `k` values |
| [medium/051 Task Scheduler](../medium/051-task-scheduler/) | Medium | Greedy on counts: at every tick, run whichever *available* task has the most copies… |
| [medium/052 Design Twitter](../medium/052-design-twitter/) | Medium | Store each user's tweets in their own list with a global timestamp, and each user's… |

## Common mistakes

- Forgetting that `heapq` is a min-heap; negate values for max-heap behavior.
- Keeping more than `k` values in a top-k min-heap, which makes its root the wrong rank.
- Popping from a heap with fewer than two items when a step requires a pair.
