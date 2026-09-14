# 074. Palindromic Substrings

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #647

## Problem

Given a string `s`, return the number of palindromic substrings in it. A substring is a contiguous run of characters, and a palindrome reads the same forwards and backwards.

Substrings with the same letters but different start or end positions count separately.

## Examples

```
Input:  s = "aaa"
Output: 6             # "a", "a", "a", "aa", "aa", "aaa"

Input:  s = "abc"
Output: 3             # only the three single characters

Input:  s = "abba"
Output: 6             # four singles, plus "bb" and "abba", both centred on the middle gap
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from checking every substring to expanding outward from each of the 2n - 1 centres and counting one palindrome per successful step, with complexity.

## Follow-up

- Return the palindromic substrings themselves (as a set of distinct strings) instead of the count. What changes about the complexity?
- Count only palindromes of length at least `k`. Where does the counter move?
- Can you get O(n) with Manacher's algorithm? What does its radius array store that expand-around-centre throws away?
