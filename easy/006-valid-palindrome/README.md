# 006. Valid Palindrome

**Difficulty:** Easy | **Pattern:** [two-pointers](../../patterns/two-pointers.md) ([explained](../../concepts/two-pointers.html)) | **Source:** LeetCode #125

## Problem

Given a string `s`, decide whether it reads the same forwards and backwards once you ignore everything that is not a letter or a digit and treat uppercase and lowercase as equal.

Return `True` if it does, `False` otherwise. A string with no alphanumeric characters at all is a palindrome.

## Examples

```
Input:  s = "No 'x' in Nixon"
Output: True          # the letters spell "noxinnixon"

Input:  s = "race a car"
Output: False         # "raceacar" reversed is "racaecar"

Input:  s = ".,;'"
Output: True          # nothing left after filtering, so vacuously a palindrome
```

## Constraints

- `0 <= s.length <= 2 * 10^5`
- `s` is printable ASCII: letters, digits, spaces, punctuation
- the empty string and a string of only punctuation both count as palindromes

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from the cleaned-copy version to the in-place two pointers, with complexity.

## Follow-up

- Building a filtered copy costs O(n) extra space. Can you decide it in O(1) space?
