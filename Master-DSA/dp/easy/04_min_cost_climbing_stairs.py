# 📘 Dynamic Programming (DP) — Easy 04
# Topic: 1D DP — Min Cost Climbing Stairs
# Approach: 1D DP
# Time: O(n) | Space: O(n) [O(1) optimized]

def min_cost_climbing_stairs(cost):
    """
    Min Cost Climbing Stairs using 1D DP.
    Returns the minimum cost to reach the top of the floor.
    You can start from index 0 or 1.
    """
    if len(cost) <= 1:
        return 0

    # dp[i] = minimum cost to reach step i (above the last step)
    # dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    # We want min cost to reach step n (the top)
    # Top is at index n, so we need dp[n]

    prev2 = 0  # dp[i-2]
    prev1 = 0  # dp[i-1]

    for i in range(2, len(cost) + 1):
        curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
        prev2 = prev1
        prev1 = curr

    return prev1


def min_cost_climbing_stairs_memo(cost, memo=None):
    """
    Min Cost Climbing Stairs using Top-Down Memoization.
    """
    if memo is None:
        memo = {}

    def dp(i):
        if i in memo:
            return memo[i]
        if i <= 1:
            return 0

        if i not in memo:
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])

        return memo[i]

    return dp(len(cost))


def min_cost_climbing_stairs_tab(cost):
    """
    Min Cost Climbing Stairs using Bottom-Up Tabulation.
    """
    if len(cost) <= 1:
        return 0

    n = len(cost)
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 0

    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    return dp[n]


if __name__ == "__main__":
    import unittest

    class TestMinCostClimbingStairs(unittest.TestCase):
        def test_min_cost_climbing_stairs(self):
            self.assertEqual(min_cost_climbing_stairs([10, 15, 20]), 15)
            self.assertEqual(min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)
            self.assertEqual(min_cost_climbing_stairs([0, 0, 0]), 0)

        def test_min_cost_climbing_stairs_memo(self):
            self.assertEqual(min_cost_climbing_stairs_memo([10, 15, 20]), 15)
            self.assertEqual(min_cost_climbing_stairs_memo([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

        def test_min_cost_climbing_stairs_tab(self):
            self.assertEqual(min_cost_climbing_stairs_tab([10, 15, 20]), 15)
            self.assertEqual(min_cost_climbing_stairs_tab([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

    # Demo
    demo = [10, 15, 20]
    print(f"Cost: {demo}")
    print(f"Minimum cost to reach top: {min_cost_climbing_stairs(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)