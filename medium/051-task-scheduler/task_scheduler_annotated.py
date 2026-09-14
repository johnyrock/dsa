import heapq
from collections import Counter, deque


class Solution:
    # Return the fewest CPU ticks needed to run every task with at least n ticks between repeats of a letter.
    def least_interval(self, tasks: list[str], n: int) -> int:
        # Only the counts matter, not which letter is which. Negate them so heapq's min-heap
        # surfaces the LARGEST remaining count at the root: that is always the best task to run next.
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)
        # Tasks that have just run and are cooling down, oldest first, as (tick when ready, negated remaining count).
        cooldown = deque()
        # The simulated clock, one tick per unit of time.
        time = 0
        # Keep going while any task is still runnable or still cooling down.
        while heap or cooldown:
            # Spend one tick, whether a task runs or the CPU idles.
            time += 1
            # If any task is ready, run the one with the most copies left.
            if heap:
                # Popping -3 and adding 1 gives -2: one copy done, two remain (still negated).
                remaining = heapq.heappop(heap) + 1
                # Zero means that letter is finished; anything else must cool down before running again.
                if remaining:
                    # It can run again once n more ticks have passed: ready at time + n, i.e. runs at time + n + 1 at the earliest.
                    cooldown.append((time + n, remaining))
            # If the CPU idles instead, nothing is popped; the tick still counts.
            # The oldest cooling task is always at the front. If its ready tick is now, move it back into the heap.
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(heap, cooldown.popleft()[1])
        # Every task has run and nothing is cooling down: the clock is the answer.
        return time
