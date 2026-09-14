# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `course_schedule_ii.py`, keep the tests, write it again.

## Key insight

A course can be taken the moment all of its prerequisites have been taken, i.e. when its indegree in the dependency graph drops to zero. Kahn's algorithm seeds a queue with every zero-indegree course, pops one at a time, appends it to `order`, and decrements the indegree of everything it unlocks, enqueueing any course that just hit zero. The pop sequence is a valid topological order by construction. Courses inside a cycle never reach zero, so if `len(order) < num_courses` at the end, no order exists and the answer is `[]`.

## Complexity

- Time: O(V + E). Building the graph touches every edge once; the loop pops every course at most once and looks at each outgoing edge once.
- Space: O(V + E) for the adjacency list, plus O(V) for `indegree`, the queue and `order`.

## Mistakes to watch for

- Building the edge as `graph[course].append(pre)` for a pair `[course, pre]`. The pair means `pre` comes first, so the edge is `pre -> course`. Reversed, the running example returns `[3, 1, 2, 0]`, which takes course 3 before either of its prerequisites.
- Returning `order` without the length check. With a cycle the queue simply runs dry early; on `n = 3, [[1,0],[2,1],[1,2]]` the loop pops only course 0 and the wrong version returns `[0]` instead of `[]`.
- Enqueueing a neighbour whenever its indegree is decremented instead of only when it reaches `0`. Course 3 in the running example would be enqueued twice (once from 1, once from 2) and appear twice in `order`.
- Seeding the queue only from courses that appear in `prerequisites`. A course with no pairs at all (isolated node) has indegree 0 and must still be in the order; iterating `range(num_courses)` covers it.

## Related

- [medium/018-course-schedule](../018-course-schedule/) is the same algorithm returning `taken == num_courses` instead of the order.
- [medium/019-clone-graph](../019-clone-graph/) is a BFS over a similar adjacency-list graph without any ordering constraint.
- [medium/010-number-of-islands](../010-number-of-islands/) is graph traversal on a grid, where the traversal order does not matter.
- Pattern doc: [patterns/topological-sort.md](../../patterns/topological-sort.md)
