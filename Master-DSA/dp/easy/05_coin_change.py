# 📘 Dynamic Programming (DP) — Easy 05
# Topic: 1D DP — Coin Change (Minimum Coins)
# Approach: 1D DP
# Time: O(amount * coins) | Space: O(amount)

def coin_change(coins, amount):
    """
    Coin Change (Minimum Number of Coins) using 1D DP.
    Returns the fewest number of coins needed to make up the amount.
    Returns -1 if it's not possible.
    """
    if amount <= 0:
        return 0

    # dp[x] = minimum number of coins to make amount x
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_combinations(coins, amount):
    """
    Coin Change (Number of Combinations) using 1D DP.
    Returns the number of combinations that make up the amount.
    """
    if amount <= 0:
        return 0

    dp = [0] * (amount + 1)
    dp[0] = 1  # One way to make 0: use no coins

    # Sort coins to ensure combinations are counted correctly
    for coin in sorted(coins):
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]

    return dp[amount]


def coin_change_memo(coins, amount, memo=None):
    """
    Coin Change (Minimum Number of Coins) using Top-Down Memoization.
    """
    if memo is None:
        memo = {}

    # Don't cache negative amounts
    if amount < 0:
        return float('inf')
    if amount in memo:
        return memo[amount]

    if amount == 0:
        return 0

    min_coins = float('inf')
    for coin in coins:
        result = coin_change_memo(coins, amount - coin, memo)
        if result != float('inf'):
            min_coins = min(min_coins, result + 1)

    memo[amount] = min_coins
    return min_coins


def coin_change_memo_optimized(coins, amount):
    """
    Coin Change (Minimum Number of Coins) using Top-Down Memoization with O(1) space for backtrack.
    """
    if amount <= 0:
        return 0

    memo = {}

    def dp(i):
        if i in memo:
            return memo[i]
        if i == 0:
            return 0
        if i < 0:
            return float('inf')

        min_coins = float('inf')
        for coin in coins:
            result = dp(i - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)

        memo[i] = min_coins
        return min_coins

    result = dp(amount)
    return result if result != float('inf') else -1


def coin_change_memo_v2(coins, amount):
    """
    Coin Change (Minimum Number of Coins) using Top-Down Memoization with proper negative handling.
    """
    if amount <= 0:
        return 0

    memo = {}

    def dp(i):
        if i in memo:
            return memo[i]
        if i == 0:
            return 0
        if i < 0:
            return float('inf')

        min_coins = float('inf')
        for coin in coins:
            res = dp(i - coin)
            if res != float('inf'):
                min_coins = min(min_coins, res + 1)

        memo[i] = min_coins
        return min_coins

    result = dp(amount)
    return result if result != float('inf') else -1


def coin_change_memo_optimized(coins, amount):
    """
    Coin Change (Minimum Number of Coins) using Top-Down Memoization with O(1) space for backtrack.
    """
    if amount <= 0:
        return 0

    memo = {}

    def dp(i):
        if i in memo:
            return memo[i]
        if i == 0:
            return 0
        if i < 0:
            return float('inf')

        min_coins = float('inf')
        for coin in coins:
            result = dp(i - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)

        memo[i] = min_coins
        return min_coins

    result = dp(amount)
    return result if result != float('inf') else -1


if __name__ == "__main__":
    import unittest

    class TestCoinChange(unittest.TestCase):
        def test_coin_change(self):
            self.assertEqual(coin_change([1, 2, 5], 11), 3)
            self.assertEqual(coin_change([2], 3), -1)
            self.assertEqual(coin_change([1], 0), 0)
            self.assertEqual(coin_change([1], 1), 1)
            self.assertEqual(coin_change([1], 2), 2)

        def test_coin_change_combinations(self):
            self.assertEqual(coin_change_combinations([1, 2, 5], 5), 4)
            self.assertEqual(coin_change_combinations([1, 2, 5], 0), 0)

        def test_coin_change_memo(self):
            self.assertEqual(coin_change_memo([1, 2, 5], 11), 3)
            self.assertEqual(coin_change_memo_v2([2], 3), -1)

    # Demo
    demo_coins = [1, 2, 5]
    demo_amount = 11
    print(f"Coins: {demo_coins}, Amount: {demo_amount}")
    print(f"Minimum coins needed: {coin_change(demo_coins, demo_amount)}")
    print(f"Number of combinations: {coin_change_combinations(demo_coins, demo_amount)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)