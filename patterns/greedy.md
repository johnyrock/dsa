# Greedy

## When to use

- The best overall answer can be built by taking the locally best choice at each step and never revisiting it.
- The problem has a "furthest reach", "earliest deadline", or "take the smallest available" flavour.
- You can argue an exchange property: swapping any optimal solution's choice for the greedy choice does not make it worse.
- A DP solution exists but the state collapses to one or two running numbers (max reach, current balance, open-count range).

## Templates

**Furthest reach in one pass (jump game):**

```python
def can_reach_end(nums):
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:          # this index is unreachable, so is the end
            return False
        farthest = max(farthest, i + jump)
    return True
```

**Layered BFS without a queue (minimum jumps):**

```python
def min_jumps(nums):
    jumps = 0
    left = right = 0               # window of indices reachable with `jumps` jumps
    while right < len(nums) - 1:
        farthest = 0
        for i in range(left, right + 1):
            farthest = max(farthest, i + nums[i])
        left, right = right + 1, farthest
        jumps += 1
    return jumps
```

**Reset on failure (gas station, partition labels):**

```python
def start_station(gas, cost):
    if sum(gas) < sum(cost):
        return -1                  # total deficit: no start works
    start = tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:               # cannot get past i from `start`
            start = i + 1          # nor from anything between start and i
            tank = 0
    return start
```

## Problems

| Problem | Difficulty | Note |
|---------|------------|------|
| [medium/086 Jump Game](../medium/086-jump-game/) | Medium | track the farthest reachable index |
| [medium/087 Jump Game II](../medium/087-jump-game-ii/) | Medium | each jump extends the window to the farthest reach seen inside it |
| [medium/088 Gas Station](../medium/088-gas-station/) | Medium | when the tank goes negative, restart after the failure point |
| [medium/089 Hand of Straights](../medium/089-hand-of-straights/) | Medium | always start a group from the smallest remaining card |
| [medium/090 Merge Triplets to Form Target Triplet](../medium/090-merge-triplets-to-form-target-triplet/) | Medium | discard triplets that exceed the target anywhere, then check each position is hit |
| [medium/091 Partition Labels](../medium/091-partition-labels/) | Medium | cut when the index reaches the last occurrence of everything seen |
| [medium/092 Valid Parenthesis String](../medium/092-valid-parenthesis-string/) | Medium | keep the range [min, max] of possible open counts; clamp min at 0 |

## Common mistakes

- Using greedy without a reason it works. If you cannot state the exchange argument, test against a small brute force.
- Off-by-one on the window bounds in Jump Game II: the loop must stop as soon as `right` covers the last index, or it counts one jump too many.
- Restarting the gas-station scan from `start + 1` instead of `i + 1`, which is O(n²) and unnecessary.
- Sorting when the input is already usable, or forgetting to sort when the greedy choice depends on order (hand of straights).
- Letting the low bound go negative in Valid Parenthesis String; a `*` treated as `)` can never make the count drop below zero.
- Confusing "some prefix is bad" with "the answer is impossible"; often the fix is to reset, not to return.
