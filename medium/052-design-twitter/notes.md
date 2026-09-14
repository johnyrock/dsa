# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete `design_twitter.py`, and write it again.

## Key insight

Store each user's tweets in their own list with a global timestamp, and each user's followees in a set. Every per-user list is already sorted by time because tweets are appended, so `get_news_feed` is a k-way merge of sorted lists: seed a max-heap (negated stamps) with the newest tweet of the user and each followee, pop the newest, and push that same author's next-older tweet in its place. Stop after 10 pops. The heap never holds more than one entry per author, and the merge touches only the tweets it actually emits, not every tweet ever posted.

## Complexity

- Time: `post_tweet`, `follow`, `unfollow` are O(1). `get_news_feed` is O(f) to seed and heapify plus O(10 log f) for the pops, where f is the number of followees (at most 500).
- Space: O(total tweets + total follow edges).

## Mistakes to watch for

- Pushing `(stamp, ...)` instead of `(-stamp, ...)`. The min-heap then yields the *oldest* first, and the running example's second feed comes back as `[5, 6]` instead of `[6, 5]`.
- Iterating only `self.following[user_id]` and forgetting `| {user_id}`. The user's own tweets vanish: the first feed is `[]` and the second is `[6]`.
- Dropping the `if idx > 0` guard. After popping an author's oldest tweet, `idx - 1 = -1` wraps around to their newest tweet, which is pushed and emitted again (`[6, 6, ...]`) until `[-2]` raises `IndexError`.
- Using `set.remove` in `unfollow`. Unfollowing someone never followed raises `KeyError`; `discard` is silent, which is what the problem expects.

## Related

- [medium/011-lru-cache](../../medium/011-lru-cache) is the other "design a class" problem here; its state panel is the model for narrating a sequence of operations.
- [easy/008-merge-two-sorted-lists](../../easy/008-merge-two-sorted-lists) is the two-way version of the merge that the heap generalises to k ways.
- [medium/049-k-closest-points-to-origin](../../medium/049-k-closest-points-to-origin) uses the same tuple-with-negated-key trick to turn `heapq` into a max-heap.
- Review the [Heap pattern](../../patterns/heap.md) and its concept page.
