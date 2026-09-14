# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `hand_of_straights.py`, keep the tests, write it again.

## Key insight

The smallest card still in hand has no smaller neighbour, so it cannot be the middle or end of any group: it must *start* one. That removes all choice. Count the cards, walk the distinct values in ascending order, and whenever a value `card` still has `need > 0` copies left, open `need` groups at once by consuming `need` copies of each of `card, card + 1, ..., card + group_size - 1`. If any of those values has fewer than `need` copies, some group cannot be completed and the answer is `False`; if the sweep finishes, every card was placed.

## Complexity

- Time: O(n log n) for the sort of distinct values; the inner loop consumes a card per iteration, so the sweep is O(n) overall (each of the n cards is decremented exactly once).
- Space: O(n) for the counter.

## Mistakes to watch for

- Anchoring on the largest card and still extending *upward*. `sorted(count, reverse=True)` opens a group `8, 9, 10` on the running example, finds no 9, and returns `False` instead of `True`. Sweeping from the top is fine only if the group is built downward.
- Consuming one copy instead of `need`: `count[c] -= 1`. On `[1,1,2,2,3,3]` with `group_size = 3` the two 1s open two groups but only one 2 and one 3 are removed, so a stray 1 and 2 remain, the sweep reaches `card = 2` with `need = 1`, needs a 4 and returns `False`; the answer is `True`.
- Checking `count[c] == 0` instead of `count[c] < need`. On `[1,1,2,3,4,4]` with `group_size = 2` the two 1s need two 2s but there is one; `== 0` lets it through, `count[2]` goes to -1, the negative count later cancels out against the 3, and the function returns `True` instead of `False`.
- Iterating over `sorted(hand)` (with duplicates) instead of `sorted(count)`. It still gives the right answer, because `need` becomes 0 for the repeats, but the inner loop runs n times instead of once per distinct value; it is the sign that the counter, not the list, is the structure being swept.

## Related

- [medium/025-top-k-frequent-elements](../025-top-k-frequent-elements) is the other problem where a `Counter` of the input is the whole state.
- [medium/051-task-scheduler](../051-task-scheduler) is a greedy over counts too, taking the most frequent first instead of the smallest value first.
- [medium/009-merge-intervals](../009-merge-intervals) shows the same "sort, then a single ordered sweep leaves no choices" argument on intervals.
- Review the [Greedy pattern](../../patterns/greedy.md) and its concept page.
