# 085. Interleaving String

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #97

## Problem

You are given three strings `s1`, `s2` and `s3`. An interleaving of `s1` and `s2` is a string built by cutting each of them into pieces and merging the pieces so that every character of both strings is used once and the characters of each string stay in their original order.

Return `True` if `s3` is an interleaving of `s1` and `s2`, otherwise `False`.

## Examples

```
Input:  s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: True          # aa|d|b|b|c|b|ca|c taken from s1,s2,s1,s2,s1,s2,s2,s1 keeps both orders

Input:  s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: False         # after "aadbbb" both strings are waiting on a c, so the a cannot be placed

Input:  s1 = "", s2 = "", s3 = ""
Output: True          # two empty strings interleave to the empty string
```

## Constraints

- `0 <= s1.length, s2.length <= 100`
- `0 <= s3.length <= 200`
- `s1`, `s2`, and `s3` consist of lowercase English letters

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from trying every split to filling a 2-D table of prefix answers one cell at a time, with complexity.

## Follow-up

- The table only ever reads the row above and the cell to the left. Can you solve it with a single row of `n + 1` booleans?
- Return one valid split (which characters came from `s1`) rather than just yes/no. What do you record while filling the table, and how do you walk it back?
- Suppose the interleaving must alternate strictly, one character from each string in turn. Which case of the recurrence disappears, and does the table still need two dimensions?
