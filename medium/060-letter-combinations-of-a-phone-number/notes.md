# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `letter_combinations_of_a_phone_number.py`, keep the tests, write it again.

## Key insight

Each output string is one letter chosen from each digit's key, in order, so it is a product of small sets. `backtrack(index)` chooses the letter for position `index`: loop over `keypad[digits[index]]`, push the letter, recurse on `index + 1`, pop. When `index == len(digits)` the path is a complete string, so join and record it. There is nothing to prune; every branch of the recursion leads to an answer, and the recursion is just a clean way to write `len(digits)` nested loops when that number is not known in advance.

## Complexity

- Time: O(4^n · n). At most 4 letters per digit gives at most 4^n strings, and joining each costs O(n).
- Space: O(n) for `path` and the recursion depth, plus the output.

## Mistakes to watch for

- Dropping `if not digits: return []`. With no digits the base case fires immediately on an empty path and the function returns `[""]`, one empty string, where the problem wants `[]`.
- Forgetting `path.pop()`. The letters accumulate across siblings, so `"23"` returns `["ad", "ade", "adef", "adefbd", ...]`, nine strings of growing length instead of nine two-letter strings.
- Indexing the keypad by position, `keypad[index]`, instead of by the digit at that position, `keypad[digits[index]]`. That is a `KeyError` on the first call.
- Writing the base case as `index == len(digits) - 1` and recording there. The last digit's letters are never chosen, so `"23"` returns `["a", "b", "c"]`.

## Related

- [medium/033-generate-parentheses](../033-generate-parentheses) has the same push / recurse / pop shape with two guards added.
- [medium/059-palindrome-partitioning](../059-palindrome-partitioning) chooses a variable-length piece per level instead of a single letter.
- [medium/047-implement-trie-prefix-tree](../047-implement-trie-prefix-tree) is the structure that would prune this search against a dictionary.
- Review the [Backtracking pattern](../../patterns/backtracking.md) and its concept page.
