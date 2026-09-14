import unittest
from design_twitter import Twitter


def run(ops):
    # ops is a list of ("post", user, tweet), ("feed", user), ("follow", a, b) or ("unfollow", a, b);
    # returns the list of feed results in order
    twitter = Twitter()
    out = []
    for op in ops:
        if op[0] == "post":
            twitter.post_tweet(op[1], op[2])
        elif op[0] == "feed":
            out.append(twitter.get_news_feed(op[1]))
        elif op[0] == "follow":
            twitter.follow(op[1], op[2])
        else:
            twitter.unfollow(op[1], op[2])
    return out


class TestDesignTwitter(unittest.TestCase):
    def test_twitter(self):
        cases = [
            # (ops, expected feed results)
            ([("post", 1, 5), ("feed", 1), ("follow", 1, 2), ("post", 2, 6), ("feed", 1),
              ("unfollow", 1, 2), ("feed", 1)], [[5], [6, 5], [5]]),                        # the running example in the walkthrough
            ([("feed", 1)], [[]]),                                                            # nobody has tweeted
            ([("follow", 1, 2), ("feed", 1)], [[]]),                                          # followee has no tweets
            ([("post", 1, 10), ("post", 2, 20), ("post", 1, 11), ("post", 2, 21), ("post", 1, 12),
              ("follow", 1, 2), ("feed", 1)], [[12, 21, 11, 20, 10]]),                        # interleaved by time, not grouped by author
            ([("post", 1, 10), ("post", 2, 20), ("follow", 1, 2), ("feed", 1), ("feed", 2)], [[20, 10], [20]]),  # feed is per user
            ([("unfollow", 1, 2), ("post", 1, 1), ("feed", 1)], [[1]]),                       # unfollow before follow must not raise
            ([("follow", 1, 2), ("follow", 1, 2), ("post", 2, 7), ("unfollow", 1, 2), ("feed", 1)], [[]]),  # double follow, one unfollow
            ([("post", 1, i) for i in range(12)] + [("feed", 1)], [[11, 10, 9, 8, 7, 6, 5, 4, 3, 2]]),  # capped at 10, newest first
            ([("post", 2, 1), ("post", 3, 2), ("post", 4, 3), ("follow", 1, 2), ("follow", 1, 3), ("follow", 1, 4),
              ("feed", 1)], [[3, 2, 1]]),                                                     # user with no tweets of their own
            ([("post", 1, 0), ("feed", 1)], [[0]]),                                           # tweet id 0 is a real tweet
        ]

        for ops, expected in cases:
            with self.subTest(ops=ops):
                result = run(ops)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
