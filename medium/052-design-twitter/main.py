from design_twitter import Twitter

twitter = Twitter()

twitter.post_tweet(1, 5)
print(twitter.get_news_feed(1))   # [5]
twitter.follow(1, 2)
twitter.post_tweet(2, 6)
print(twitter.get_news_feed(1))   # [6, 5]
twitter.unfollow(1, 2)
print(twitter.get_news_feed(1))   # [5]
