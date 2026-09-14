# 066. Course Schedule II

**Difficulty:** Medium | **Pattern:** [topological-sort](../../patterns/topological-sort.md) ([explained](../../concepts/topological-sort.html)) | **Source:** LeetCode #210

## Problem

There are `numCourses` courses labelled `0` to `numCourses - 1`. Each pair `[a, b]` in `prerequisites` means you must take course `b` before course `a`.

Return an ordering of all the courses in which every prerequisite is taken before the course that needs it. If several valid orderings exist, return any one of them. If it is impossible to finish every course (the prerequisites contain a cycle), return an empty list.

## Examples

```
Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0, 1, 2, 3]  # 0 first (no prerequisites), then 1 and 2 (both need 0), then 3 (needs both); [0, 2, 1, 3] is also valid

Input:  numCourses = 2, prerequisites = [[1,0]]
Output: [0, 1]        # take 0, then 1

Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: []            # 0 needs 1 and 1 needs 0: no order can satisfy both
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= ai, bi < numCourses`
- `ai != bi`
- all pairs `[ai, bi]` are distinct

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from trying every permutation to Kahn's algorithm that repeatedly takes a course with no unmet prerequisites and records the order it took them in, with complexity.

## Follow-up

- Kahn's algorithm is BFS. Write the DFS version: post-order on the dependency graph, reversed, with a three-colour visited array to detect cycles. Which is easier to get right under time pressure?
- Return the *lexicographically smallest* valid order. What do you swap the queue for, and what does that cost?
- Instead of one valid order, return the minimum number of semesters needed if any number of courses can be taken per semester (LeetCode #1136). Which quantity in Kahn's loop already tracks this?
