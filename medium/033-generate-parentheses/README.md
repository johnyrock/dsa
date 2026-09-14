# 033. Generate Parentheses

**Difficulty:** Medium | **Pattern:** [backtracking](../../patterns/backtracking.md) ([explained](../../concepts/backtracking.html)) | **Source:** LeetCode #22

## Problem

Given an integer `n`, return every string made of exactly `n` opening and `n` closing parentheses that is well-formed, meaning every `)` closes a `(` that came before it. Each string has length `2n`.

Return the strings in any order; there must be no duplicates.

## Examples

```
Input:  n = 1
Output: ["()"]                 # the only pair

Input:  n = 2
Output: ["(())", "()()"]       # nested or side by side; ")(" and "))((" are not well-formed

Input:  n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]   # 5 = the 3rd Catalan number
```

## Constraints

- `1 <= n <= 8`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from enumerating all 2^(2n) strings to the two-guard backtracking that only ever builds valid prefixes, with complexity.

## Follow-up

- The answer count is the Catalan number C(n). Can you count the strings in O(n) without generating them?
- Suppose there are two kinds of brackets, `()` and `[]`, with `n` pairs of each. What extra state does the recursion need, and how does the output count change?
- Instead of a list `path` with `append`/`pop`, pass the string itself (`backtrack(s + "(", ...)`). What does that cost per call, and why does it still work without an explicit undo?
