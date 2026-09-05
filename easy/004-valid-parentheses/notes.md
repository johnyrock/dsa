# Notes

## Attempts

- 2026-09-05: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. First review should be a from-scratch re-solve with the solution file deleted, before any confidence score is trusted.

## Key insight

Counting brackets is not enough, because counts ignore order. The real rule is that the most recently opened bracket must be the next one closed, and that is exactly last-in-first-out, which is a stack. A dict from closer to opener turns "does this closer match?" into one comparison.

## Complexity

- Time: O(n), each character is pushed at most once and popped at most once.
- Space: O(n) for the stack, worst case a string of all openers like `"((((("`.

## Mistakes to watch for

- Check `not stack` before popping, or a leading closer like `")"` raises IndexError on an empty stack.
- Returning True at the end of the loop is wrong; return `not stack` so leftover openers like `"(("` fail.
- Map closer to opener, not opener to closer. The lookup happens when a closing bracket arrives.

## Related

- Min Stack and Daily Temperatures use the same "keep the pending items on a stack" shape.
- Longest Valid Parentheses (hard) stacks indices instead of characters to measure spans.
