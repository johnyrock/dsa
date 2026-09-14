# 070. Network Delay Time

**Difficulty:** Medium | **Pattern:** [graph](../../patterns/graph.md) ([explained](../../concepts/graph-traversal.html)) | **Source:** LeetCode #743

## Problem

A network has `n` nodes labelled `1` to `n`. `times[i] = [u, v, w]` says a signal sent from `u` reaches `v` after `w` units of time; edges are directed. A signal is sent from node `k`.

Return the minimum time until every node has received the signal, or `-1` if some node can never receive it.

## Examples

```
Input:  times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2             # 2->1 at time 1, 2->3 at time 1, 3->4 at time 2; the slowest arrival is 2

Input:  times = [[1,2,1]], n = 2, k = 1
Output: 1             # the only other node is one hop away

Input:  times = [[1,2,1]], n = 2, k = 2
Output: -1            # the edge points into 2, so 1 is never reached
```

## Constraints

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= u, v <= n`, `u != v`
- `0 <= w <= 100`
- all `(u, v)` pairs are unique

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from relaxing every edge `n - 1` times to Dijkstra's algorithm with a min-heap, with complexity.

## Follow-up

- Weights here are non-negative. Which line of Dijkstra breaks if an edge can have a negative weight, and what algorithm replaces it?
- If every `w` were 1, could you drop the heap entirely? What traversal computes the same answer?
- How would you return the actual path along which the last node received the signal, not just the time?
