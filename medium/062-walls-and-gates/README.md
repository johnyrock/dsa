# 062. Walls and Gates

**Difficulty:** Medium | **Pattern:** [graph](../../patterns/graph.md) ([explained](../../concepts/graph-traversal.html)) | **Source:** LeetCode #286

## Problem

You are given an `m × n` grid `rooms` where each cell is one of three values: `-1` is a wall or obstacle, `0` is a gate, and `INF = 2147483647` is an empty room.

Fill each empty room with the distance to its nearest gate, moving up, down, left or right through empty rooms only. If a room cannot reach any gate, leave it as `INF`. Modify `rooms` in place and return nothing.

## Examples

```
Input:  rooms = [
  [INF,  -1,   0, INF],
  [INF, INF, INF,  -1],
  [INF,  -1, INF,  -1],
  [  0,  -1, INF, INF],
]
Output: rooms = [
  [3, -1, 0, 1],
  [2,  2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3,  4],
]                     # (0, 0) is 3 steps from the gate at (3, 0); (3, 3) is 4 steps from the gate at (0, 2)

Input:  rooms = [[-1]]
Output: rooms = [[-1]] # a wall stays a wall

Input:  rooms = [[INF, -1, 0]]
Output: rooms = [[INF, -1, 0]]  # the wall cuts the room off; it keeps INF
```

## Constraints

- `m == rooms.length`
- `n == rooms[i].length`
- `1 <= m, n <= 250`
- `rooms[i][j]` is `-1`, `0`, or `2^31 - 1`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from one search per room to a single breadth-first search that starts from every gate at once, with complexity.

## Follow-up

- What changes if each room should record *which* gate is nearest, not just how far it is?
- If moving through a cell could cost more than 1 (a weighted grid), why does the queue stop being enough, and what replaces it?
- How would you answer "the farthest room from any gate" without a second pass over the grid?
