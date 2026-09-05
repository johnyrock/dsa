# Notes

## Attempts

- 2026-09-05: Folder generated as reference material, not solved independently. The solution, annotated version and walkthrough were written up front rather than reached by attempting the problem, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `contains_duplicate.py`, keep the tests, write it again.

## Key insight

Don't compare pairs. Walk once and ask a membership question instead: "have I already seen this exact value?" A set answers that in O(1), so one pass decides it. Checking before adding is what stops an element from matching itself.

## Complexity

- Time: O(n), one pass with O(1) membership checks. Early exit on the first repeat, so a duplicate near the front costs far less than the worst case.
- Space: O(n) for the set when every value is distinct.

## Mistakes to watch for

- Check `n in seen` before `seen.add(n)`, or every element matches itself and the answer is always `True`.
- `len(set(nums)) != len(nums)` is correct and short, but it always builds the whole set. The loop can bail out on the second element.
- Sorting first and scanning neighbours works and uses O(1) extra space, but it costs O(n log n) and mutates the input unless you copy it.
- Return a bool, not the duplicate value or its index. That is a different problem.

## Related

- Contains Duplicate II adds a distance constraint on the indices, so the set becomes a sliding window.
- Valid Anagram and Longest Consecutive Sequence use the same "membership in O(1)" reflex.
- Two Sum (easy/001) is the hash *map* version: same reflex, but it stores an index alongside the value.
