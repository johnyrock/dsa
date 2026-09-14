# 059. Palindrome Partitioning

**Difficulty:** Medium | **Pattern:** [backtracking](../../patterns/backtracking.md) ([explained](../../concepts/backtracking.html)) | **Source:** LeetCode #131

## Problem

Given a string `s`, split it into consecutive substrings such that every piece is a palindrome. Return every such partition as a list of its pieces, in the order they appear in `s`.

Return the partitions in any order.

## Examples

```
Input:  s = "aab"
Output: [["a","a","b"],["aa","b"]]   # "ab" and "aab" are not palindromes, so b is always alone

Input:  s = "a"
Output: [["a"]]                      # a single character is its own palindrome

Input:  s = "aba"
Output: [["a","b","a"],["aba"]]      # "ab" and "ba" are not palindromes, so the only other cut is none
```

## Constraints

- `1 <= s.length <= 16`
- `s` contains only lowercase English letters

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from trying every set of cut positions to a recursion that extends the current piece only while it is a palindrome, with complexity.

## Follow-up

- `is_palindrome(start, end)` is recomputed for the same pair from different partitions. Precompute a `pal[i][j]` table in O(n^2) first; how does that change the total time, and for which inputs does it matter?
- Palindrome Partitioning II (LeetCode #132) asks only for the *minimum* number of cuts. Why does enumeration become the wrong tool, and what replaces it?
- The number of partitions of `"aaaaaaaaaaaaaaaa"` (16 a's) is 2^15 = 32768. Can you argue that every partition of any string is reachable by this recursion exactly once?
