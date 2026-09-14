# 034. Daily Temperatures

**Difficulty:** Medium | **Pattern:** [stack](../../patterns/stack.md) ([explained](../../concepts/stack.html)) | **Source:** LeetCode #739

## Problem

You are given an array `temperatures` where `temperatures[i]` is the temperature on day `i`. For each day, find how many days you have to wait until a strictly warmer temperature.

Return an array `answer` of the same length where `answer[i]` is that wait, or `0` if no warmer day ever comes.

## Examples

```
Input:  temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]      # day 2 (75) waits until day 6 (76): 6 - 2 = 4; days 6 and 7 never get warmer

Input:  temperatures = [30,40,50,60]
Output: [1,1,1,0]              # every day is beaten by the next one

Input:  temperatures = [30,60,90]
Output: [1,1,0]
```

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from scanning forward for every day to a monotonic stack of unresolved indices, with complexity.

## Follow-up

- The temperatures are bounded to `30..100`. Can you solve it with a 71-entry "next occurrence" table walked from the right instead of a stack, and what is its complexity?
- Change "strictly warmer" to "warmer or equal". Which single character in the solution changes, and what happens to `[70,70,70]`?
- Instead of the wait in days, return the *temperature* of the next warmer day (or `-1`). Does the stack need to hold anything different?
