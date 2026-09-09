# 002. Valid Anagram

**Difficulty:** Easy | **Pattern:** [hash-map](../../patterns/hash-map.md) ([explained](../../concepts/hash-map.html)) | **Source:** LeetCode #242

## Problem

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s` and `False` otherwise.

An anagram uses exactly the same letters as the original, the same number of times, in any order. Case matters and every character counts, so the two strings must be the same length.

## Examples

```
Input:  s = "anagram", t = "nagaram"
Output: True          # same letters: a×3, n, g, r, m

Input:  s = "rat", t = "car"
Output: False         # t has a c, s does not

Input:  s = "aa", t = "a"
Output: False         # different lengths
```

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters
- the two strings may have different lengths

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from sorting both strings to the one-pass character count, with complexity.

## Follow-up

- Sorting is O(n log n). Can you do it in O(n)?
- What changes if the input is Unicode instead of 26 lowercase letters?
