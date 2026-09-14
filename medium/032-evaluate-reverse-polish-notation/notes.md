# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `evaluate_reverse_polish_notation.py`, keep the tests, write it again.

## Key insight

In postfix notation an operator always applies to the two values computed most recently before it, so a stack of pending operands is the whole state. Numbers are pushed; an operator pops two values (the top is the right operand, the one under it is the left), applies itself, and pushes the result back. After the last token a valid expression leaves exactly one value on the stack, and that is the answer. No parentheses or precedence rules are needed because the token order already encodes them.

## Complexity

- Time: O(n), each token is pushed at most once and popped at most once.
- Space: O(n), the stack can hold up to about n / 2 + 1 operands before the operators arrive.

## Mistakes to watch for

- Swapping the operands. Writing `a, b = stack.pop(), stack.pop()` then `a - b` computes `right - left`; on `["5","3","-"]` that returns `-2` instead of `2`, and on the running example `int(5 / 13) = 0` gives `4` instead of `6`. Pop the right operand first.
- Using `//` for division. Python floors toward negative infinity, but the problem truncates toward zero: `6 // -132` is `-1`, `int(6 / -132)` is `0`. The third LeetCode example returns `12` instead of `22` with `//`.
- Treating `"-11"` as the minus operator by testing `token[0] == "-"` or `not token.isdigit()`. Compare against the four operator strings exactly, and let `int(token)` parse everything else, sign included.
- Returning `stack.pop()` inside the loop, or `stack[0]`, instead of `stack[-1]` after the loop. A single-operand expression like `["3"]` still needs the push and the final read.

## Related

- `easy/004-valid-parentheses` is the same stack pattern applied to matching brackets instead of evaluating operators.
- `medium/031-min-stack` is another stack whose contents evolve with a sequence of operations.
- `medium/006-add-two-numbers` also builds a numeric result one piece at a time from an unusual encoding.
- Pattern doc: `patterns/stack.md`
