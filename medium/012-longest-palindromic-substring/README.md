# 012. Longest Palindromic Substring

**Difficulty:** Medium | **Pattern:** [two-pointers](../../patterns/two-pointers.md) ([explained](../../concepts/two-pointers.html)) | **Source:** LeetCode #5

## Problem

Given a string `s`, return the longest substring of `s` that is a palindrome. A palindrome reads the same forwards and backwards.

If several palindromic substrings tie for longest, any one of them is accepted.

## Examples

```
Input:  s = "babad"
Output: "bab"          # "aba" is also accepted

Input:  s = "cbbd"
Output: "bb"           # an even-length palindrome

Input:  s = "a"
Output: "a"
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of digits and English letters
- a single character is a palindrome, so the answer is never empty

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from testing every substring to expanding outward from each of the 2n − 1 centres, with complexity.

## Follow-up

- Every palindrome has a centre. How many possible centres does a string of length n have, and why is that number not n?
- Manacher's algorithm does this in O(n). What does it reuse that expand-around-centre throws away?
