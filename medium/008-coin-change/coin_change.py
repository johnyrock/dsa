def coin_change(coins, amount):
    INF = amount + 1  # more coins than any real answer can need
    dp = [INF] * (amount + 1)
    dp[0] = 0  # zero coins make amount 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] != INF else -1
