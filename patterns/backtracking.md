# Backtracking

## When to use

- The problem asks for *all* solutions (every subset, permutation, combination, partition) rather than the best one or a count.
- A candidate is built one choice at a time and a partial candidate can be rejected early ("prune") before it is complete.
- The search space is exponential but small enough to enumerate (`n` up to about 20 for subsets, about 10 for permutations).
- Classic signals: "generate all", "return every valid", "find any path/placement that works" on a grid or board.

## Templates

**Include / exclude (subsets, combination sum):**

```python
def subsets(nums):
    out = []
    path = []

    def dfs(i):
        if i == len(nums):
            out.append(path[:])        # copy: path keeps mutating after this
            return
        path.append(nums[i])           # choose nums[i]
        dfs(i + 1)
        path.pop()                     # undo the choice
        dfs(i + 1)                     # skip nums[i]

    dfs(0)
    return out
```

**Loop over the next choice with a start index (combinations, no duplicate sets):**

```python
def combination_sum(candidates, target):
    out = []
    path = []

    def dfs(start, remaining):
        if remaining == 0:
            out.append(path[:])
            return
        for j in range(start, len(candidates)):
            if candidates[j] > remaining:      # prune: cannot fit
                continue
            path.append(candidates[j])
            dfs(j, remaining - candidates[j])  # j (not j + 1) allows reuse
            path.pop()

    dfs(0, target)
    return out
```

**Used-set for permutations, with a skip rule for duplicates:**

```python
def permutations(nums):
    nums.sort()                        # sorting makes equal values adjacent
    out = []
    path = []
    used = [False] * len(nums)

    def dfs():
        if len(path) == len(nums):
            out.append(path[:])
            return
        for j in range(len(nums)):
            if used[j]:
                continue
            # duplicate rule: same value as the previous one, and the previous
            # one is not in the current path -> this branch was already explored
            if j > 0 and nums[j] == nums[j - 1] and not used[j - 1]:
                continue
            used[j] = True
            path.append(nums[j])
            dfs()
            path.pop()
            used[j] = False

    dfs()
    return out
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [medium/033 Generate Parentheses](../medium/033-generate-parentheses/) | Medium | add `(` while opens remain, add `)` only while closes < opens |
| [medium/053 Subsets](../medium/053-subsets/) | Medium | include / exclude each element |
| [medium/054 Combination Sum](../medium/054-combination-sum/) | Medium | start index stays at `j` so a candidate can be reused |
| [medium/055 Permutations](../medium/055-permutations/) | Medium | used array, path complete when its length is `n` |
| [medium/056 Subsets II](../medium/056-subsets-ii/) | Medium | sort, then skip a value equal to the previous one at the same depth |
| [medium/057 Combination Sum II](../medium/057-combination-sum-ii/) | Medium | sort, start at `j + 1`, skip equal neighbours at the same depth |
| [medium/058 Word Search](../medium/058-word-search/) | Medium | DFS on the grid, mark the cell visited, restore it on the way back |
| [medium/059 Palindrome Partitioning](../medium/059-palindrome-partitioning/) | Medium | try every prefix that is a palindrome, recurse on the rest |
| [medium/060 Letter Combinations of a Phone Number](../medium/060-letter-combinations-of-a-phone-number/) | Medium | one loop level per digit over its letters |

## Common mistakes

- Appending `path` itself instead of `path[:]`. Every stored result then aliases the same list and ends up empty.
- Forgetting to undo the choice (`pop`, `used[j] = False`, restore the grid cell) so later branches see a stale state.
- Passing `j + 1` when reuse is allowed, or `j` when it is not.
- Handling duplicates by deduplicating the output at the end. Sort and skip at the same depth instead; it is both faster and easier to justify.
- In grid search, marking the cell visited *after* recursing, which lets the same cell be used twice in a word.
- Recursing past the prune point (e.g. continuing a loop after `remaining` went negative) and only discovering the failure at the leaf.
