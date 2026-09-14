# 051. Task Scheduler

**Difficulty:** Medium | **Pattern:** [heap](../../patterns/heap.md) ([explained](../../concepts/heap.html)) | **Source:** LeetCode #621

## Problem

You are given an array of CPU `tasks`, each an uppercase letter, and a non-negative integer `n`. Each unit of time the CPU either runs one task or sits idle. Two runs of the *same* task must be separated by at least `n` other time units (other tasks or idles). Tasks can be run in any order.

Return the minimum number of time units needed to finish every task.

## Examples

```
Input:  tasks = ["A","A","A","B","B","B"], n = 2
Output: 8             # A B idle A B idle A B: after each A, two slots must pass before the next A

Input:  tasks = ["A","C","A","B","D","B"], n = 1
Output: 6             # A B A C B D, no idles needed because there are enough different letters

Input:  tasks = ["A","A","A","B","B","B"], n = 3
Output: 10            # A B idle idle A B idle idle A B
```

## Constraints

- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter
- `0 <= n <= 100`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from trying every ordering to a max-heap of remaining counts plus a cooldown queue that simulates the CPU one tick at a time, with complexity.

## Follow-up

- There is an O(n) closed form: `max(len(tasks), (max_count - 1) * (n + 1) + number_of_tasks_with_max_count)`. Derive it from the simulation, and say why the `max` with `len(tasks)` is needed.
- The simulation ticks through idle slots one at a time. How would you jump straight to the next ready time when the heap is empty?
- Task Scheduler II (LeetCode #2365) fixes the order of the tasks. Which half of this solution survives, and which becomes a hash map of "next allowed time"?
