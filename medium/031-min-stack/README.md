# 031. Min Stack

**Difficulty:** Medium | **Pattern:** [stack](../../patterns/stack.md) ([explained](../../concepts/stack.html)) | **Source:** LeetCode #155

## Problem

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element, each in constant time.

Implement the `MinStack` class: `MinStack()` creates an empty stack, `push(val)` pushes `val`, `pop()` removes the top element, `top()` returns the top element, and `getMin()` returns the smallest element currently in the stack. Every operation must run in O(1) time. (This repo spells it `get_min`.)

## Examples

```
Input:  ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]
Output: [null,null,null,null,-3,null,0,-2]
        # after pushing -2, 0, -3 the min is -3; pop removes -3, so top is 0 and the min falls back to -2

Input:  ["MinStack","push","push","pop","getMin"]
        [[],[1],[1],[],[]]
Output: [null,null,null,null,1]
        # two copies of 1; popping one must not lose the minimum for the other

Input:  ["MinStack","push","push","push","getMin","pop","getMin"]
        [[],[3],[1],[2],[],[],[]]
Output: [null,null,null,null,1,null,1]
        # popping 2 (not the minimum) leaves the minimum at 1
```

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- `pop`, `top` and `getMin` are always called on non-empty stacks
- at most `3 * 10^4` calls in total to `push`, `pop`, `top` and `getMin`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from scanning the stack on every `getMin` to a second stack that records each new minimum, with complexity.

## Follow-up

- The `min_stack` can be as large as `stack` when values arrive in decreasing order. Can you store just one number per element instead, by pushing `(val, current_min)` pairs? What does that trade?
- There is an O(1)-extra-space trick that stores `2 * val - min` on a single stack. Why does it need arbitrary-precision integers, and where does it break in a 32-bit language?
- How would you support `getMax` as well without touching the existing `get_min` logic?
