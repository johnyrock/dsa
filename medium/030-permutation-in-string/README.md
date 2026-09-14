# 030. Permutation in String

**Difficulty:** Medium | **Pattern:** [sliding-window](../../patterns/sliding-window.md) ([explained](../../concepts/sliding-window.html)) | **Source:** LeetCode #567

## Problem

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1` as a contiguous substring, and `false` otherwise.

In other words: is there some window of `s2`, exactly `len(s1)` characters wide, whose letters are a rearrangement of `s1`'s letters?

## Examples

```
Input:  s1 = "ab", s2 = "eidbaooo"
Output: true           # s2 contains "ba", a permutation of "ab"

Input:  s1 = "ab", s2 = "eidboaoo"
Output: false          # 'a' and 'b' both appear but are never adjacent

Input:  s1 = "adc", s2 = "dcda"
Output: true           # the window "cda" has the same letter counts as "adc"
```

## Constraints

- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters only

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from sorting every substring to sliding a fixed-width window with letter counts, with complexity.

## Follow-up

- The solution compares two 26-slot arrays on every step. How would you keep a single `matches` counter (0–26) updated incrementally so each step is O(1) rather than O(26)?
- Find All Anagrams in a String (LeetCode #438) asks for every start index instead of a yes/no. What changes in the loop?
- If the alphabet were arbitrary Unicode instead of 26 lowercase letters, what would you replace the fixed-size arrays with, and what does the equality check cost then?
