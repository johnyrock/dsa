# Hash Map

## When to use

- You need to answer "have I seen X before?" in O(1) while scanning once.
- You need to count occurrences or group items by a computed key.
- A brute-force nested loop is comparing every element against every other; a map often collapses the inner loop.

## Template

```python
seen = {}
for i, x in enumerate(items):
    key = f(x)               # what would make a match with x?
    if key in seen:
        ...                  # found a match, use seen[key]
    seen[g(x)] = i           # record x for later elements
```

Check before insert when an element must not match itself.

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [easy/001 Two Sum](../easy/001-two-sum/) | Easy | value -> index, look up the complement |

## Common mistakes

- Inserting before checking, which lets an element pair with itself.
- Using a list for membership tests, which is O(n) per lookup and turns O(n) back into O(n²).
