class Solution:
    # Count the combinations of coins (order does not matter, unlimited supply of each) that add up to amount.
    def change(self, amount: int, coins: list[int]) -> int:
        # dp[a] is the number of combinations that make amount a using only the coins processed so far. Starts at 0 everywhere.
        dp = [0] * (amount + 1)  # dp[a]: combinations that make amount a using the coins seen so far
        # The empty combination makes amount 0, and it is the seed every other count grows from.
        dp[0] = 1  # one way to make 0: use no coins
        # Coins on the outside. Finishing one coin completely before starting the next is what makes {1, 2} and {2, 1} the same combination instead of two.
        for coin in coins:
            # Amounts smaller than the coin cannot use it, so start at coin. Going upward lets dp[a - coin] already include this coin, which is the unlimited-supply rule.
            for a in range(coin, amount + 1):
                # Every combination for a - coin becomes a combination for a by adding one more of this coin.
                dp[a] += dp[a - coin]
        # After all coins, dp[amount] counts every combination.
        return dp[amount]
