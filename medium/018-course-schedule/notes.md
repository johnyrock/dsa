# Notes

## Attempts

- 2026-09-12: Folder generated as reference material, not solved independently. First review should be a from-scratch re-solve: delete `course_schedule.py`, keep the tests, write it again.

## Key insight

Finishing all courses is possible exactly when the prerequisite graph has no cycle. Kahn's algorithm detects this without explicit cycle detection: repeatedly take any course with zero remaining prerequisites, then decrement the indegree of everything that depended on it. If every course eventually gets taken, there was no cycle — courses inside a cycle never reach indegree 0, since each depends on another course inside the same cycle.

## Complexity

- Time: O(V + E) — V courses, E prerequisite edges, each visited once.
- Space: O(V + E) for the graph and indegree array.

## Mistakes to watch for

- Building the edge in the wrong direction. `[a, b]` means `b` must come before `a`, i.e. the edge is `b -> a` in the dependency graph, not `a -> b`.
- Forgetting courses with zero prerequisites from the start — they need to seed the queue, not just courses that later reach indegree 0.
- Comparing `taken == num_courses` at the end, not just checking whether the queue emptied — an empty queue happening early (due to a cycle) still needs to be distinguished from a full completion.

## Related

- Clone Graph (medium) is a different traversal (BFS/DFS) over a similar adjacency-list graph, without dependency ordering.
- Course Schedule II (medium, LeetCode #210) is the same algorithm, returning the order instead of a boolean.
