class Solution:
    # Define the function that takes the coin denominations and a target and returns the fewest coins that make it, or -1.
    def coin_change(self, coins: list[int], amount: int) -> int:
        # A sentinel meaning "not reachable yet". amount + 1 works because the worst real answer is amount coins of value 1, so anything larger is impossible.
        INF = amount + 1  # more coins than any real answer can need
        # dp[a] = fewest coins that make exactly a. One slot per amount from 0 up to the target.
        dp = [INF] * (amount + 1)
        # Base case: making 0 needs no coins. Every other answer is built by adding coins on top of this.
        dp[0] = 0  # zero coins make amount 0
        # Fill the table upward. By the time we compute dp[a], every smaller amount is already final.
        for a in range(1, amount + 1):
            # Try each coin as the LAST coin in an optimal pile for a.
            for c in coins:
                # The coin must fit, and using it must actually improve on what we have.
                if c <= a and dp[a - c] + 1 < dp[a]:
                    # If a - c is reachable in dp[a - c] coins, then a is reachable in one more.
                    dp[a] = dp[a - c] + 1
        # If the target slot was never improved from the sentinel, no combination of coins reaches it.
        return dp[amount] if dp[amount] != INF else -1
