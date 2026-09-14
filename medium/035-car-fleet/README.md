# 035. Car Fleet

**Difficulty:** Medium | **Pattern:** [stack](../../patterns/stack.md) ([explained](../../concepts/stack.html)) | **Source:** LeetCode #853

## Problem

`n` cars are driving along a one-lane road toward a destination `target` miles away. Car `i` starts at mile `position[i]` and drives at `speed[i]` miles per hour. A car can never pass the car ahead of it: when it catches up, it slows to match and the two drive on as a single *fleet* (a fleet can be one car). A car that catches another exactly at the target still counts as part of that fleet.

Return the number of fleets that arrive at the target.

## Examples

```
Input:  target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3             # 10 and 8 meet at 12 (both take 1h); 5 and 3 meet at 6 (3 catches 5 by t=1, then crawl at speed 1); 0 alone

Input:  target = 10, position = [3], speed = [3]
Output: 1             # one car is one fleet

Input:  target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1             # the car at 4 is slowest and in front; everyone catches it
```

## Constraints

- `n == position.length == speed.length`
- `1 <= n <= 10^5`
- `0 < target <= 10^6`
- `0 <= position[i] < target`
- all values of `position` are unique
- `0 < speed[i] <= 10^6`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from simulating the road tick by tick to sorting by position and keeping a stack of fleet arrival times, with complexity.

## Follow-up

- Car Fleet II (LeetCode #1776) asks for the *time* at which each car collides with the next one. Why does the stack need to hold more than an arrival time there?
- The stack only ever compares against its top and is never popped. Can you replace it with a single float and a counter, and does anything change in the complexity?
- What if cars could overtake but you were asked how many *pairs* of cars ever meet before the target? Which part of the current reasoning stops applying?
