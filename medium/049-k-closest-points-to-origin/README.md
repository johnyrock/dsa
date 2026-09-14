# 049. K Closest Points to Origin

**Difficulty:** Medium | **Pattern:** [heap](../../patterns/heap.md) ([explained](../../concepts/heap.html)) | **Source:** LeetCode #973

## Problem

You are given an array `points` where `points[i] = [xi, yi]` is a point on the plane, and an integer `k`. The distance between two points is the ordinary Euclidean distance `sqrt((x1 - x2)^2 + (y1 - y2)^2)`.

Return the `k` points closest to the origin `(0, 0)`. The answer is guaranteed to be unique except for the order, and it may be returned in any order.

## Examples

```
Input:  points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]     # squared distances 18, 26, 20; the two smallest are 18 and 20

Input:  points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]           # 1^2 + 3^2 = 10 versus 2^2 + 2^2 = 8, so [-2,2] is closer

Input:  points = [[0,1],[1,0]], k = 2
Output: [[0,1],[1,0]]      # k equals the number of points, so everything is returned
```

## Constraints

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from sorting every point by distance to a max-heap capped at `k` entries, with complexity.

## Follow-up

- Quickselect on the squared distances gives O(n) average time. When would you prefer it over the heap, and when would you not?
- If the points arrive as a stream and `k` is small, which of the two approaches still works?
- How would you change the heap if the query asked for the `k` points *farthest* from the origin instead?
