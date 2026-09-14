import heapq
from collections import defaultdict


class Twitter:
    def __init__(self) -> None:
        # A global counter stamped onto every tweet, so "more recent" means "larger stamp" regardless of author.
        self.time = 0
        # user_id -> list of (stamp, tweet_id), oldest first. Appending keeps each list sorted by stamp for free.
        self.tweets = defaultdict(list)
        # follower_id -> set of followee ids. A set makes follow, unfollow and membership O(1).
        self.following = defaultdict(set)

    # Record a tweet by user_id and advance the clock.
    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        # The stamp is captured before the increment, so the first tweet ever is stamp 0.
        self.tweets[user_id].append((self.time, tweet_id))
        self.time += 1

    # Return up to 10 tweet ids from the user and everyone they follow, most recent first.
    def get_news_feed(self, user_id: int) -> list[int]:
        # One heap entry per author: that author's NEWEST tweet. Negated stamp makes heapq's min-heap return the newest first.
        heap = []
        # The user sees their own tweets too, so union the follow set with {user_id}.
        for uid in self.following[user_id] | {user_id}:
            # Skip authors who have never tweeted; there is nothing to seed.
            if self.tweets[uid]:
                # idx is the position of the newest tweet in that author's list.
                idx = len(self.tweets[uid]) - 1
                stamp, tweet_id = self.tweets[uid][idx]
                # Carry uid and idx so that after popping this tweet we can push the same author's next-older one.
                heap.append((-stamp, tweet_id, uid, idx))
        # Build the heap in O(authors) rather than pushing one at a time.
        heapq.heapify(heap)
        feed = []
        # Stop as soon as 10 tweets are collected or every author is exhausted.
        while heap and len(feed) < 10:
            # The root is the newest tweet among all authors' current candidates.
            _, tweet_id, uid, idx = heapq.heappop(heap)
            feed.append(tweet_id)
            # If that author has an older tweet, it becomes their new candidate. idx > 0 guards the start of the list.
            if idx > 0:
                stamp, older_id = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-stamp, older_id, uid, idx - 1))
        return feed

    # Add followee to the follower's set. A set ignores duplicate follows.
    def follow(self, follower_id: int, followee_id: int) -> None:
        self.following[follower_id].add(followee_id)

    # discard, not remove: unfollowing someone never followed must not raise.
    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.following[follower_id].discard(followee_id)
