class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)  # dp[a]: combinations that make amount a using the coins seen so far
        dp[0] = 1  # one way to make 0: use no coins
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]
        return dp[amount]
