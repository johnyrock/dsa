# 003. Longest Substring Without Repeating Characters

**Difficulty:** Medium | **Pattern:** [sliding-window](../../patterns/sliding-window.md) | **Source:** LeetCode #3

## Problem

Given a string `s`, return the length of the longest substring that contains no repeated character.

A substring is contiguous. `"abc"` is a substring of `"abcabcbb"`; `"acb"` is not.

## Examples

```
Input:  s = "abcabcbb"
Output: 3             # "abc", the later "bca" and "cab" tie

Input:  s = "bbbbb"
Output: 1             # every character is the same, so any single "b"

Input:  s = "pwwkew"
Output: 3             # "wke"; "pwke" is a subsequence, not a substring
```

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces
- the empty string has answer 0

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from checking every substring to a sliding window whose left edge jumps straight past the repeat, with complexity.

## Follow-up

- The simple window shrinks one character at a time. Can you make the left edge jump directly to the right place?
- What if `s` were a stream and you could only see each character once?
