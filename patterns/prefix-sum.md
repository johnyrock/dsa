# Prefix Sum / Prefix Product

## When to use

- The answer at position i depends on an aggregate (sum, product, max) of everything to its left, or to its right, or both.
- You are about to write a nested loop where the inner loop recomputes the same running total for each i.
- Range queries: "sum of `nums[l..r]`" many times over a fixed array.

## Template

```python
# Left-to-right running aggregate written into the output BEFORE folding in nums[i]
prefix = identity            # 0 for sums, 1 for products
for i in range(n):
    result[i] = prefix       # aggregate of everything strictly left of i
    prefix = combine(prefix, nums[i])

# Right-to-left pass multiplies (or adds) the mirror aggregate on top
suffix = identity
for i in range(n - 1, -1, -1):
    result[i] = combine(result[i], suffix)
    suffix = combine(suffix, nums[i])
```

For range sums, build `pre[i] = sum(nums[:i])` once; then `sum(nums[l:r+1]) == pre[r + 1] - pre[l]`.

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [medium/002 Product of Array Except Self](../medium/002-product-of-array-except-self/) | Medium | left products in one sweep, right products multiplied on top, no division |

## Common mistakes

- Folding `nums[i]` into the running value before writing it out, so a slot includes itself.
- Using 0 as the identity for a product, or 1 for a sum.
- Off-by-one in the reverse loop: `range(n - 1, -1, -1)` reaches index 0.
- Reaching for division to "undo" a total. It is forbidden in Product Except Self and breaks on zeros anyway.
