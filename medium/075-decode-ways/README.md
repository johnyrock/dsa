# 075. Decode Ways

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #91

## Problem

A message of letters `A`–`Z` was encoded by mapping `A -> "1"`, `B -> "2"`, ..., `Z -> "26"` and concatenating the digits. Given the digit string `s`, return the number of ways it can be decoded back into letters.

A grouping is valid only if every piece is a code from `1` to `26`; pieces like `"0"`, `"06"`, or `"27"` are not codes. If no valid decoding exists, return `0`.

## Examples

```
Input:  s = "226"
Output: 3             # "BZ" (2 | 26), "VF" (22 | 6), "BBF" (2 | 2 | 6)

Input:  s = "12"
Output: 2             # "AB" (1 | 2) or "L" (12)

Input:  s = "06"
Output: 0             # "6" would be F, but "06" is not a code and a lone "0" is not either
```

## Constraints

- `1 <= s.length <= 100`
- `s` contains only digits and may contain leading zeros

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from the exponential recursion over "take one digit or two" to the two-variable bottom-up count with the zero rules, with complexity.

## Follow-up

- Decode Ways II (LeetCode #639) adds a `*` wildcard that stands for any digit `1`–`9`. Which of the two branches gets more complicated, and by how much?
- Return one valid decoding (or all of them) instead of the count. Why does that blow up the complexity?
- If the alphabet had 100 letters (codes `1`–`100`), how many rolling variables would you need?
