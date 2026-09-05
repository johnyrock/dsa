# 004. Valid Parentheses

**Difficulty:** Easy | **Pattern:** [stack](../../patterns/stack.md) | **Source:** LeetCode #20

## Problem

Given a string `s` made up only of the characters `(`, `)`, `[`, `]`, `{` and `}`, decide whether the brackets are balanced.

A string is balanced when every bracket is closed by the matching kind of bracket, and the closings happen in the right order: the bracket that opened most recently is always the one that closes next.

## Examples

```
Input:  s = "()"
Output: true

Input:  s = "([]{})"
Output: true          # each closer matches the most recent opener

Input:  s = "([)]"
Output: false         # right counts, wrong order
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` contains only the six bracket characters
- an odd-length string can never be valid

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from counting brackets to the stack, with complexity.

## Follow-up

- Counting opens and closes is O(n) too. What exactly does the stack know that a counter does not?
