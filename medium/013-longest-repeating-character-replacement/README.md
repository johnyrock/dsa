# 013. Longest Repeating Character Replacement

**Difficulty:** Medium | **Pattern:** [sliding-window](../../patterns/sliding-window.md) ([explained](../../concepts/sliding-window.html)) | **Source:** LeetCode #424

## Problem

Given a string `s` and an integer `k`, you may replace up to `k` characters with any other uppercase letter. Return the length of the longest substring achievable where every character is the same after those replacements.

## Examples

```
Input:  s = "ABAB", k = 2
Output: 4        # replace both A's, or both B's

Input:  s = "AABABBA", k = 1
Output: 4        # "AABA" or "ABBB", one replacement
```

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of uppercase English letters only
- `0 <= k <= s.length`

## Walkthrough

Open [walkthrough.html](walkthrough.html) for a scroll-driven narration of the sliding window and why it never needs to shrink its record.

## Follow-up

- Why is it safe that `max_count` is never decremented when the window shrinks?
- What changes if letters can be lowercase and uppercase, treated as distinct?
