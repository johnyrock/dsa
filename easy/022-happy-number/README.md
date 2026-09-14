# 022. Happy Number

**Difficulty:** Easy | **Pattern:** [fast-slow-pointers](../../patterns/fast-slow-pointers.md) ([explained](../../concepts/fast-slow-pointers.html)) | **Source:** LeetCode #202

## Problem

Starting from a positive integer `n`, repeatedly replace the number with the sum of the squares of its decimal digits. Either the process reaches `1` and stays there, or it falls into a loop that never includes `1`.

Return `true` if `n` eventually reaches `1` (it is "happy"), and `false` if it loops forever.

## Examples

```
Input:  n = 19
Output: true          # 1+81=82, 64+4=68, 36+64=100, 1+0+0=1

Input:  n = 2
Output: false         # 4, 16, 37, 58, 89, 145, 42, 20, 4 ... loops

Input:  n = 1
Output: true          # already there
```

## Constraints

- `1 <= n <= 2^31 - 1`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the digit-square sequence, the visited-set approach, and the tortoise-and-hare replacement that uses O(1) space.

## Follow-up

- Every unhappy number falls into the same cycle `4, 16, 37, 58, 89, 145, 42, 20`. Can you use that fact to replace the two runners with a single check?
- Why can the sequence never grow without bound? What is the largest value a 10-digit input can map to in one step?
- What changes if the digits are read in a base other than 10?
