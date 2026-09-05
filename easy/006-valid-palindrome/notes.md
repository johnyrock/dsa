# Notes

## Attempts

- 2026-09-05: Folder generated as reference material, not solved independently. The solution, the annotated version and the walkthrough were written up front rather than derived from an attempt, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `valid_palindrome.py`, keep the tests, write it again.

## Key insight

A palindrome check only ever compares mirrored positions, so there is no need to build a cleaned copy of the string. Two pointers walk inward from both ends, each skipping non-alphanumeric characters in place, and the comparison is done on `.lower()` of whatever they land on. Filtering becomes a movement rule instead of a new string, which drops the space from O(n) to O(1).

## Complexity

- Time: O(n). Each pointer only ever moves inward, so together they cross each position at most once.
- Space: O(1). Two integer indices, no copy of the string.

## Mistakes to watch for

- The inner skip loops need their own `left < right` guard. Without it, a string with no alphanumerics at all (`".,;'"`) walks a pointer off the end and raises `IndexError`.
- Lowercase both sides before comparing, not just one.
- `isalnum()` is the right test, not `isalpha()` — digits count, so `"12321"` is a palindrome.
- `'0'.lower()` is `'0'`, not `'p'`. `"0P"` is False; watch for solutions that compare character codes with a sloppy case fix.
- The empty string and a whitespace-only string are both True; the `while left < right` condition handles that without a special case.

## Related

- Valid Palindrome II (easy/medium) allows one deletion, same two-pointer skeleton with a branch.
- Two Sum II (sorted input) uses the same inward-walking pointers to hit a target sum.
- Reverse String and Container With Most Water are the other standard two-pointer drills.
