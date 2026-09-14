# 081. Longest Common Subsequence

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #1143

## Problem

You are given two strings `text1` and `text2`. A subsequence is what is left of a string after deleting zero or more characters without reordering the rest, and a common subsequence is one that appears in both strings.

Return the length of the longest common subsequence, or `0` if there is none.

## Examples

```
Input:  text1 = "abcde", text2 = "ace"
Output: 3             # "ace" is a subsequence of both; nothing longer fits inside "ace"

Input:  text1 = "abc", text2 = "abc"
Output: 3             # identical strings share everything

Input:  text1 = "abc", text2 = "def"
Output: 0             # no character in common
```

## Constraints

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from trying every subsequence to filling a 2-D prefix table, with complexity.

## Follow-up

- The table only ever reads the previous row. Can you get the space down to O(min(m, n)) while keeping the same time?
- Return the subsequence itself, not just its length. What do you need to keep, and how do you walk it back from `dp[m][n]`?
- Edit Distance (LeetCode #72) uses the same table shape with three transitions instead of two. Which line changes, and why does the mismatch case cost 1 there but 0 here?
