import heapq
from collections import defaultdict


class Twitter:
    def __init__(self) -> None:
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.tweets[user_id].append((self.time, tweet_id))
        self.time += 1

    def get_news_feed(self, user_id: int) -> list[int]:
        heap = []
        for uid in self.following[user_id] | {user_id}:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                stamp, tweet_id = self.tweets[uid][idx]
                heap.append((-stamp, tweet_id, uid, idx))
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            _, tweet_id, uid, idx = heapq.heappop(heap)
            feed.append(tweet_id)
            if idx > 0:
                stamp, older_id = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-stamp, older_id, uid, idx - 1))
        return feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.following[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.following[follower_id].discard(followee_id)
