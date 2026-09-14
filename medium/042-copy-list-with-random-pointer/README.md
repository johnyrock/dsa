# 042. Copy List with Random Pointer

**Difficulty:** Medium | **Pattern:** [hash-map](../../patterns/hash-map.md) ([explained](../../concepts/hash-map.html)) | **Source:** LeetCode #138

## Problem

A linked list of length `n` is given where each node has a `val`, a `next` pointer, and an extra `random` pointer that can point to any node in the list or to `null`. Construct a deep copy of the list: `n` brand-new nodes whose `next` and `random` pointers reproduce the original's shape, but none of which is a node from the original list.

Return the head of the copied list. The list is given as an array of `[val, random_index]` pairs, where `random_index` is the 0-based position the random pointer targets, or `null`.

## Examples

```
Input:  head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]   # same shape, but every node is new

Input:  head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]                            # both randoms point at the second node

Input:  head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]                # equal values, distinct nodes; identity matters, not val
```

## Constraints

- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or points to a node in the linked list

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of why a plain copy fails, the old-node-to-new-node map, the two passes, pitfalls, and complexity.

## Follow-up

- Can you do it in O(1) extra space by interleaving each copy right after its original (`A → A' → B → B' → …`), then splitting the lists apart?
- What if the `random` pointer could target a node in a *different* list? What does the map need to contain then?
- How would you verify a deep copy in a test — what does "no node is shared" look like as an assertion?
