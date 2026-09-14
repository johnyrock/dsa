# 032. Evaluate Reverse Polish Notation

**Difficulty:** Medium | **Pattern:** [stack](../../patterns/stack.md) ([explained](../../concepts/stack.html)) | **Source:** LeetCode #150

## Problem

You are given an array of strings `tokens` that represents an arithmetic expression in Reverse Polish Notation (postfix): every operator follows its two operands, so `["2","1","+"]` means `2 + 1`. The operators are `+`, `-`, `*`, `/`, and every operand is an integer.

Evaluate the expression and return the result as an integer. Division between two integers truncates toward zero, there is never a division by zero, and the expression is always valid.

## Examples

```
Input:  tokens = ["4","13","5","/","+"]
Output: 6              # 4 + (13 / 5) = 4 + 2, since 13 / 5 = 2.6 truncates to 2

Input:  tokens = ["2","1","+","3","*"]
Output: 9              # (2 + 1) * 3

Input:  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22             # ((10 * (6 / ((9 + 3) * -11))) + 17) + 5; 6 / -132 truncates to 0, not -1
```

## Constraints

- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator `"+"`, `"-"`, `"*"`, `"/"`, or an integer in the range `[-200, 200]`
- the expression is valid RPN, so an operator always has two operands available
- the intermediate results and the answer fit in a 32-bit integer

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from rewriting the expression in place to a single pass with a stack of pending operands, with complexity.

## Follow-up

- Why does postfix notation need no parentheses and no precedence table, when infix (`2 + 1 * 3`) needs both?
- How would you convert an infix expression to RPN (the shunting-yard algorithm), and what does a second stack hold in that conversion?
- If the tokens arrived one at a time from a stream, could you still evaluate without buffering the whole expression? What is the maximum stack depth for a valid expression of `n` tokens?
