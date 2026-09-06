# Notes

## Attempts

- 2026-09-06: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete `lru_cache.py`, keep the tests, write it again.

## Key insight

Two structures, each covering the other's weakness. A dictionary finds a key in O(1) but has no notion of order. A doubly linked list keeps recency order and can move or remove a node in O(1), but cannot find a key. Store `key -> node` in the dictionary so a lookup lands directly on the node, then unlink it and push it to the front. The least recently used entry is always the node just before the tail sentinel. Nodes carry their key so eviction can also delete from the dictionary.

## Complexity

- Time: O(1) for both `get` and `put`. Every step is a dictionary operation or a constant number of pointer changes.
- Space: O(capacity) for the nodes and dictionary entries.

## Mistakes to watch for

- Using a singly linked list. Unlinking a node in O(1) needs its predecessor, so `prev` pointers are required.
- No sentinels. Without dummy head and tail, inserting at the front and removing the last real node each need empty-list special cases, and that is where bugs hide.
- Forgetting that `get` is a use. A hit must move the node to the front, otherwise a hot key can be evicted.
- On `put` of an existing key, inserting a second node instead of updating the first. The map would point at the new one while the old one sits in the list, and the size accounting drifts.
- Evicting before checking whether the key already exists. Updating a key never changes the size, so it should never evict.
- Not storing the key on the node. When the tail node is evicted you need its key to delete the dictionary entry.
- Python's `OrderedDict` (`move_to_end`, `popitem(last=False)`) solves this in ten lines. Know it, mention it, but expect to be asked for the explicit version.

## Related

- Reverse Linked List (easy/007) and Merge Two Sorted Lists (easy/008) build the pointer-rewiring habit this relies on.
- LFU Cache (LeetCode #460) adds a frequency count and one recency list per frequency.
- Design Browser History and Min Stack are other "design" problems where the trick is pairing two structures.
