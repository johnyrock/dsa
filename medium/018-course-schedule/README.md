# 018. Course Schedule

**Difficulty:** Medium | **Pattern:** [topological-sort](../../patterns/topological-sort.md) ([explained](../../concepts/topological-sort.html)) | **Source:** LeetCode #207

## Problem

There are `numCourses` courses labeled `0` to `numCourses - 1`. Each pair `[a, b]` in `prerequisites` means you must take course `b` before course `a`. Return whether it's possible to finish all courses.

## Examples

```
Input:  numCourses = 2, prerequisites = [[1,0]]
Output: true

Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false     # 0 needs 1, 1 needs 0 — a cycle
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- all pairs are unique

## Walkthrough

Open [walkthrough.html](walkthrough.html) for a scroll-driven narration of Kahn's algorithm (BFS topological sort via indegree).

## Follow-up

- Return an actual valid course order, not just whether one exists (LeetCode #210).
