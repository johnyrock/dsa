# 039. Time Based Key-Value Store

**Difficulty:** Medium | **Pattern:** [binary-search](../../patterns/binary-search.md) ([explained](../../concepts/binary-search.html)) | **Source:** LeetCode #981

## Problem

Design a key-value store that keeps every value ever written to a key, each tagged with the timestamp it was written at, and can answer "what was the value of this key at time t?".

- `TimeMap()` creates the store.
- `set(key, value, timestamp)` records that `key` had `value` from `timestamp` onward.
- `get(key, timestamp)` returns the value written at the largest timestamp that is `<= timestamp`. If the key has no write that old (or was never set), return `""`.

All timestamps passed to `set` for a given key are strictly increasing.

## Examples

```
TimeMap()
set("foo", "bar", 1)      # foo: [(1, "bar")]
set("foo", "bar2", 4)     # foo: [(1, "bar"), (4, "bar2")]
set("foo", "bar3", 7)     # foo: [(1, "bar"), (4, "bar2"), (7, "bar3")]
get("foo", 4)  -> "bar2"  # exact match on timestamp 4
get("foo", 5)  -> "bar2"  # no write at 5; the latest write at or before 5 is the one at 4
get("foo", 0)  -> ""      # every write is newer than 0
get("foo", 9)  -> "bar3"  # the newest write overall
```

```
TimeMap()
set("foo", "bar", 1)
get("foo", 1)  -> "bar"
get("foo", 3)  -> "bar"   # still the value from time 1
set("foo", "bar2", 4)
get("foo", 4)  -> "bar2"
get("foo", 5)  -> "bar2"
```

## Constraints

- `1 <= key.length, value.length <= 100`
- `key` and `value` consist of lowercase English letters and digits
- `1 <= timestamp <= 10^7`
- all timestamps of `set` are strictly increasing
- at most `2 * 10^5` calls to `set` and `get`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from scanning a key's history to a per-key sorted list searched with a rightmost-`<=` binary search, with complexity.

## Follow-up

- Drop the guarantee that timestamps arrive in increasing order. What does `set` have to do now, and what does it cost? (Python's `bisect.insort` is a hint, and so is its O(n) shifting.)
- Add `delete(key, timestamp)` that removes a single historical write. Which representation makes that cheap, and what happens to the binary search?
- Snapshot Array (LeetCode #1146) asks for the value of an array slot at a given snapshot id. Why is it the same problem with a different vocabulary?
