# Stack

## When to use

- The most recently opened thing must be handled first (matching brackets, undo, nested structures).
- You need to look back at the "previous unresolved item" while scanning forward.
- Parsing anything nested or recursive without recursion.

## Template

```python
stack = []
for x in items:
    if opens(x):
        stack.append(x)
    else:
        if not stack or not matches(stack[-1], x):
            return False
        stack.pop()
return not stack       # anything left open is a failure
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/004 Valid Parentheses](../easy/004-valid-parentheses/) | Easy | map closer to opener, pop on match |
| [medium/031 Min Stack](../medium/031-min-stack/) | Medium | The minimum of a stack only changes at two moments: when a new value at or below the… |
| [medium/032 Evaluate Reverse Polish Notation](../medium/032-evaluate-reverse-polish-notation/) | Medium | In postfix notation an operator always applies to the two values computed most… |
| [medium/034 Daily Temperatures](../medium/034-daily-temperatures/) | Medium | Walk the days left to right and keep a stack of indices whose warmer day has not… |
| [medium/035 Car Fleet](../medium/035-car-fleet/) | Medium | Whether a car joins the fleet ahead of it depends only on arrival times: compute `time… |

## Common mistakes

- Popping from an empty stack. Check `if not stack` before `pop()`.
- Returning `True` at the end of the loop without checking the stack is empty.
- Counting opens and closes instead of tracking order. `([)]` has balanced counts but is invalid.
