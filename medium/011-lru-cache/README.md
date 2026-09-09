# 011. LRU Cache

**Difficulty:** Medium | **Pattern:** [linked-list](../../patterns/linked-list.md) ([explained](../../concepts/linked-list.html)) | **Source:** LeetCode #146

## Problem

Design a data structure that behaves like a Least Recently Used cache with a fixed `capacity`.

- `LRUCache(capacity)` creates the cache.
- `get(key)` returns the value stored under `key`, or `-1` if it is not present. A successful `get` counts as a use.
- `put(key, value)` stores or updates the value. If the insert pushes the cache past `capacity`, evict the least recently used key first. A `put` counts as a use.

Both operations must run in O(1) average time.

## Examples

```
LRUCache(2)
put(1, 1)          # cache: {1}
put(2, 2)          # cache: {1, 2}
get(1)   -> 1      # 1 is now the most recently used
put(3, 3)          # capacity exceeded, evict 2 (least recently used)
get(2)   -> -1     # gone
put(4, 4)          # evict 1
get(1)   -> -1
get(3)   -> 3
get(4)   -> 4
```

## Constraints

- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`, `0 <= value <= 10^5`
- up to `2 * 10^5` calls to `get` and `put`
- `get` and `put` must each be O(1)

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from a dictionary with timestamps to a hash map pointing into a doubly linked list ordered by recency, with complexity.

## Follow-up

- Python's `OrderedDict` has `move_to_end` and `popitem(last=False)`. Why is it fine to mention and risky to lean on in an interview?
- LFU Cache (LeetCode #460) evicts by frequency instead of recency. What extra structure does that need?
