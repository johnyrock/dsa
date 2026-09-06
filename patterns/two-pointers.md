# Two Pointers

## When to use

- Comparing elements from both ends of a sequence (palindromes, reversing in place), or growing outward from a centre.
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

**Sorted pair search (Two Sum II, the inner loop of 3Sum):**

```python
left, right = i + 1, len(nums) - 1
while left < right:
    total = nums[left] + nums[right]
    if total < target:
        left += 1
    elif total > target:
        right -= 1
    else:
        record(left, right)
        left += 1
        right -= 1
```

Move the pointer that can still improve the answer. In 3Sum that is decided by the sum; in Container With Most Water it is always the shorter wall.

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/006 Valid Palindrome](../easy/006-valid-palindrome/) | Easy | skip non-alphanumerics, compare lowercase |
| [medium/004 3Sum](../medium/004-3sum/) | Medium | sort, fix i, close left/right on the rest, skip duplicates |
| [medium/005 Container With Most Water](../medium/005-container-with-most-water/) | Medium | start at the ends, always move the shorter wall |
| [medium/012 Longest Palindromic Substring](../medium/012-longest-palindromic-substring/) | Medium | expand outward from each of the 2n - 1 centres while the ends match |

## Common mistakes

- Advancing both pointers when only one should move.
- Using `<=` where `<` is correct, or vice versa. When pointers meet there is nothing left to compare.
- Forgetting to normalise case before comparing.
- In 3Sum, skipping duplicates by looking forward (`nums[i] == nums[i + 1]`) instead of backward, which drops the first copy.
- In Container With Most Water, moving the taller wall. Only moving the shorter one can raise the ceiling.
- In Longest Palindromic Substring, skipping the even-length (gap) centres, or using `right - left + 1` after the pointers have overshot.
