# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete `task_scheduler.py`, and write it again.

## Key insight

Greedy on counts: at every tick, run whichever *available* task has the most copies left, because the letter with the most copies is the one that will force idles later if it falls behind. A max-heap of negated counts answers "most copies left" in O(log 26). A task that just ran is not available for `n` ticks, so it leaves the heap and waits in a FIFO `cooldown` queue tagged with the tick it becomes ready; because every task waits exactly `n` ticks, the queue is naturally sorted and only its front ever needs checking. The clock advances one tick per loop whether or not something ran, and the clock at the end is the answer.

## Complexity

- Time: O(T · log 26) where T is the answer (total ticks including idles). Each tick does at most one pop and one push on a heap of at most 26 entries, so effectively O(T). The closed form `max(len(tasks), (max_count - 1) * (n + 1) + count_of_max)` is O(len(tasks)).
- Space: O(26) for the counts, heap, and queue: O(1).

## Mistakes to watch for

- Looping `while heap:` instead of `while heap or cooldown:`. At tick 2 on the running example the heap is empty while both letters are cooling down, so the loop exits and returns 2 instead of 8.
- Marking the ready tick as `time + n - 1` (or comparing with `<` instead of `==`). A that ran at tick 1 then re-runs at tick 3 with only one slot between, giving 6 instead of 8; the gap must contain `n` *other* ticks, so ready is `time + n` and the re-run happens at `time + n + 1`.
- Pushing the popped count back into the heap immediately (`heappush(heap, remaining)` in the same tick) instead of into the queue. The same letter is then eligible every tick and the answer is just `len(tasks)`.
- Forgetting the `if remaining:` guard and queueing `(time + n, 0)` for a finished letter. When that `0` comes back and is popped, `0 + 1 = 1` is truthy, so it is re-queued as a phantom task with a growing count and the loop never terminates.

## Related

- [easy/019-last-stone-weight](../../easy/019-last-stone-weight) is the same negated max-heap, drained instead of recycled.
- [medium/025-top-k-frequent-elements](../../medium/025-top-k-frequent-elements) also starts from `Counter` and feeds counts into a heap.
- [easy/021-meeting-rooms](../../easy/021-meeting-rooms) is another time-slot feasibility problem, solved by sorting instead of simulation.
- Review the [Heap pattern](../../patterns/heap.md) and its concept page.
