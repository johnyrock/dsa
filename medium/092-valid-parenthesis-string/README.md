# 092. Valid Parenthesis String

**Difficulty:** Medium | **Pattern:** [greedy](../../patterns/greedy.md) ([explained](../../concepts/greedy.html)) | **Source:** LeetCode #678

## Problem

You are given a string `s` made of `'('`, `')'` and `'*'`. Every `'*'` may be treated as a single `'('`, a single `')'`, or an empty string, independently of the other stars.

Return `true` if some choice for the stars makes `s` a valid parenthesis string: every `'('` has a matching `')'` after it, every `')'` has a matching `'('` before it, and the string is balanced.

## Examples

```
Input:  s = "(*))"
Output: true          # read the star as '(' to get "(())"

Input:  s = "(*)"
Output: true          # the star can be empty, giving "()"

Input:  s = "(((*)"
Output: false         # three opens, and one star plus one ')' can close at most two of them
```

## Constraints

- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'` or `'*'`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from trying all three readings of every star to a single pass that carries the lowest and highest possible open count.

## Follow-up

- Return one concrete valid assignment of the stars, not just `true`. Which of the two bounds tells you which way each star should go?
- Solve it without the `lo`/`hi` trick, with two passes: left to right treating stars as `'('`, then right to left treating them as `')'`. Why is that equivalent?
- What if each `'*'` could also stand for `"()"`, two characters at once? How do the bound updates change?
