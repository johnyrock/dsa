# 060. Letter Combinations of a Phone Number

**Difficulty:** Medium | **Pattern:** [backtracking](../../patterns/backtracking.md) ([explained](../../concepts/backtracking.html)) | **Source:** LeetCode #17

## Problem

Given a string `digits` containing digits from `2` to `9`, return every string that the digits could represent on a classic phone keypad, where `2` maps to `abc`, `3` to `def`, `4` to `ghi`, `5` to `jkl`, `6` to `mno`, `7` to `pqrs`, `8` to `tuv`, and `9` to `wxyz`. Each output string takes one letter from each digit's key, in order.

Return the strings in any order. An empty `digits` yields an empty list.

## Examples

```
Input:  digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]   # 3 letters for 2 × 3 letters for 3 = 9 strings

Input:  digits = ""
Output: []                                               # no digits means no strings, not one empty string

Input:  digits = "2"
Output: ["a","b","c"]                                    # one key, one letter each
```

## Constraints

- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from enumerating every letter string to a recursion that picks one letter per digit, with complexity.

## Follow-up

- Write the same enumeration without recursion: start from `[""]` and, for each digit, replace the list with every string extended by every letter of that key. Is the order of the output the same?
- Suppose the keypad also had `1` and `0` mapping to no letters. Should a `1` in the input contribute nothing (skip it) or make the answer empty? How does each choice change the recursion?
- With a dictionary of valid English words, how would you stop exploring a prefix that no word starts with? Which structure from this repo gives that check in O(1) per letter?
