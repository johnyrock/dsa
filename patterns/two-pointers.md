# Two Pointers

## When to use

- Comparing elements from both ends of a sequence (palindromes, reversing in place).
- Sorted input where moving one pointer inward narrows the search (pair sums, removing duplicates).
- You want O(1) extra space instead of building a filtered copy.

## Template

```python
left, right = 0, len(items) - 1
while left < right:
    if skip(items[left]):
        left += 1
    elif skip(items[right]):
        right -= 1
    elif items[left] != items[right]:
        return False
    else:
        left += 1
        right -= 1
return True
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/006 Valid Palindrome](../easy/006-valid-palindrome/) | Easy | skip non-alphanumerics, compare lowercase |

## Common mistakes

- Advancing both pointers when only one should move.
- Using `<=` where `<` is correct, or vice versa. When pointers meet there is nothing left to compare.
- Forgetting to normalise case before comparing.
