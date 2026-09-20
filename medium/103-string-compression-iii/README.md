# 103. String Compression III

**Difficulty:** Medium | **Pattern:** [two-pointers](../../patterns/two-pointers.md) ([explained](../../concepts/two-pointers.html)) | **Source:** LeetCode #3163

## Problem

Given a string `word`, compress it by repeatedly removing the longest prefix made of a single repeated character, but at most 9 copies at a time, and appending the prefix's length followed by that character to the result. Return the compressed string.

This is run-length encoding with the count written first and every count kept to a single digit: a run of 14 `a`s becomes `9a5a`, not `14a`.

## Examples

```
Input:  word = "aabbdd"
Output: "2a2b2d"        # three runs of length 2: "aa", "bb", "dd"

Input:  word = "abcde"
Output: "1a1b1c1d1e"    # every run has length 1, and a count of 1 is still written

Input:  word = "aaaaaaaaaaaaaabb"
Output: "9a5a2b"        # 14 a's are split into a run of 9 and a run of 5
```

## Constraints

- `1 <= word.length <= 2 * 10^5`
- `word` consists only of lowercase English letters

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from slicing prefixes off a shrinking string to two same-direction pointers that measure each run in place, with complexity.

## Follow-up

- Drop the cap of 9. What changes in the output format, and why does decoding become ambiguous if counts and characters can both be digits?
- Write the decoder: given `"9a5a2b"`, rebuild `"aaaaaaaaaaaaaabb"`. Can you do it in one pass without knowing the output length up front?
- LeetCode #443 String Compression writes the character first, omits counts of 1, and must be done in place in a `list[str]`. How does the read pointer / write pointer pair change when the output overwrites the input?
