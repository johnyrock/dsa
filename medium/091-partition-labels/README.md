# 091. Partition Labels

**Difficulty:** Medium | **Pattern:** [greedy](../../patterns/greedy.md) ([explained](../../concepts/greedy.html)) | **Source:** LeetCode #763

## Problem

You are given a string `s`. Split it into as many contiguous parts as possible so that each letter appears in at most one part; concatenating the parts in order must give back `s`.

Return a list of the sizes of those parts.

## Examples

```
Input:  s = "ababcbacadefegdehijhklij"
Output: [9,7,8]       # "ababcbaca" | "defegde" | "hijhklij"; every letter stays inside one part

Input:  s = "eccbbbbdec"
Output: [10]          # 'e' and 'c' both reappear at the very end, so nothing can be split off

Input:  s = "abc"
Output: [1,1,1]       # no letter repeats, so every letter is its own part
```

## Constraints

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from testing every cut point against every letter to one pass that extends a running "must reach" boundary from a last-index map.

## Follow-up

- Instead of the sizes, return the actual substrings. Does the algorithm change?
- What if `s` could contain any Unicode character instead of 26 lowercase letters? What replaces the fixed-size map?
- Suppose each letter is allowed to appear in at most *two* parts. Is a greedy pass still enough?
