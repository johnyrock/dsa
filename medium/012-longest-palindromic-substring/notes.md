# Notes

## Attempts

- 2026-09-06: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete `longest_palindromic_substring.py`, keep the tests, write it again.

## Key insight

Every palindrome is symmetric around a centre, and there are only 2n − 1 centres: n characters (odd-length palindromes) and n − 1 gaps between characters (even-length ones). From each centre, push two pointers outward while the characters match. Each expansion step confirms a longer palindrome for free, because the inside was already confirmed. The longest palindrome found from any centre is the answer.

## Complexity

- Time: O(n²). 2n − 1 centres, and each expansion is at most O(n).
- Space: O(1). Two pointers and a best-so-far; the slice is taken once at the end.

## Mistakes to watch for

- Forgetting even-length centres. `"cbbd"` has no odd-length palindrome longer than 1; the answer `"bb"` is centred on the gap between the two b's.
- Off-by-one on the length. The `while` loop stops when the pointers no longer match, so the palindrome is `s[left + 1 : right]` and its length is `right - left - 1`, not `right - left + 1`.
- Checking `s[left] == s[right]` before checking bounds, which raises on `left = -1` or silently wraps in Python.
- Slicing `s[left:right]` inside the loop to compare lengths. It works but turns O(1) bookkeeping into O(n) per step.
- The DP table (`is_pal[i][j] = s[i] == s[j] and is_pal[i+1][j-1]`) is also O(n²) time but O(n²) space and slower in practice. Expand-around-centre is the expected answer; Manacher's O(n) is a bonus mention, not a requirement.

## Related

- Valid Palindrome (easy/006) is the same two-pointer comparison moving inward instead of outward.
- Palindromic Substrings (LeetCode #647) counts palindromes with the exact same expansion; every successful step adds one.
- Longest Palindromic Subsequence (LeetCode #516) drops the contiguity requirement and becomes a genuine 2D DP.
