# 052. Design Twitter

**Difficulty:** Medium | **Pattern:** [heap](../../patterns/heap.md) ([explained](../../concepts/heap.html)) | **Source:** LeetCode #355

## Problem

Design a simplified Twitter where users can post tweets, follow and unfollow each other, and see a news feed.

- `Twitter()` creates the object.
- `post_tweet(user_id, tweet_id)` posts a new tweet by `user_id`. Each call has a unique `tweet_id`.
- `get_news_feed(user_id)` returns the 10 most recent tweet ids in the user's feed, most recent first. The feed contains tweets by the user and by every user they follow.
- `follow(follower_id, followee_id)` and `unfollow(follower_id, followee_id)` update who follows whom.

## Examples

```
Twitter()
post_tweet(1, 5)
get_news_feed(1)   -> [5]       # only their own tweet
follow(1, 2)
post_tweet(2, 6)
get_news_feed(1)   -> [6, 5]    # 6 was posted after 5, so it comes first
unfollow(1, 2)
get_news_feed(1)   -> [5]       # user 2's tweets are gone from the feed

Twitter()
post_tweet(1, 10), post_tweet(2, 20), post_tweet(1, 11), post_tweet(2, 21), post_tweet(1, 12)
follow(1, 2)
get_news_feed(1)   -> [12, 21, 11, 20, 10]   # interleaved by posting order, not grouped by author
```

## Constraints

- `1 <= user_id, follower_id, followee_id <= 500`
- `0 <= tweet_id <= 10^4`
- all tweet ids are unique
- at most `3 * 10^4` calls in total to `post_tweet`, `get_news_feed`, `follow`, and `unfollow`
- a user cannot follow themselves

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from scanning and sorting every tweet on each feed request to a per-user tweet list, a follow set, and a k-way heap merge that stops after 10 tweets, with complexity.

## Follow-up

- With `f` followees who each have `m` tweets, the heap merge is O(f + 10 log f) per feed. What does a solution that keeps a pre-merged feed per user cost on `post_tweet` instead, and when is that trade worth it?
- Tweets are timestamped with a global counter. What breaks if two servers each keep their own counter, and how would you fix ordering across them?
- How would you add `delete_tweet(tweet_id)` without making `get_news_feed` slower?
