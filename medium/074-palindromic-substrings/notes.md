# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `palindromic_substrings.py`, keep the tests, write it again.

## Key insight

Every palindrome has a centre: a character for odd length, the gap between two characters for even length, so `2n - 1` centres in all. From each centre push `left` and `right` outward while the characters match; every successful match is exactly one palindrome (`s[left:right + 1]`), and no palindrome is ever produced from two different centres. So `total += 1` inside the `while` loop counts each one once. This is the same expansion as Longest Palindromic Substring, but the counter replaces the "best so far" bookkeeping.

## Complexity

- Time: O(n²), 2n - 1 centres and at most n/2 steps from each. Most expansions stop on the first mismatch.
- Space: O(1), two pointers and a counter.

## Mistakes to watch for

- Running only the odd expansion `(centre, centre)`. Every even-length palindrome is missed: `"aaa"` gives 4 instead of 6, `"abba"` gives 4 instead of 6.
- Counting once per centre instead of once per matching step. `total += 1` after the `while` loop gives at most `2n - 1`: `"aaa"` returns 5 instead of 6, because the centre at index 1 produces both `"a"` and `"aaa"` and needs two increments.
- Comparing `s[left] == s[right]` before checking `left >= 0`. Python's `s[-1]` is the last character, not an error: on `"bab"` the odd expansion from index 0 compares `s[-1] = "b"` with `s[1] = "a"` (a miss), but on `"aba"` the even run `(0, 1)` fails, then the odd run from index 2 compares `s[1] = "b"` with `s[3]`, which raises `IndexError`. Bounds first, always.
- Using a set of substrings to dedupe. The problem counts positions, not distinct strings, so `"aaa"` must be 6, not 3.

## Related

- [Longest Palindromic Substring](../012-longest-palindromic-substring) (medium/012) is the same expand-around-centre loop, keeping the longest instead of counting.
- [Palindrome Partitioning](../059-palindrome-partitioning) (medium/059) uses the same palindrome test inside a backtracking search.
- [Valid Palindrome](../../easy/006-valid-palindrome) (easy/006) is the two-pointer check on a whole string.
- Pattern doc: [dynamic-programming](../../patterns/dynamic-programming.md).
