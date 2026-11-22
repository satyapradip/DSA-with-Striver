# 📘 Dynamic Programming (DP) — Easy 02
# Topic: 1D DP — House Robber
# Approach: 1D DP with state optimization
# Time: O(n) | Space: O(1)

def rob(nums):
    """
    House Robber using 1D DP with O(1) space.
    You cannot rob adjacent houses.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    # dp[i] = max amount we can rob up to house i
    # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    prev2 = 0  # dp[i-2]
    prev1 = 0  # dp[i-1]

    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = curr

    return prev1


def rob_memo(nums, memo=None):
    """
    House Robber using Top-Down Memoization.
    """
    if memo is None:
        memo = {}

    def dp(i):
        if i in memo:
            return memo[i]
        if i < 0:
            return 0

        # Either rob current house and skip previous, or skip current
        memo[i] = max(dp(i - 1), nums[i] + dp(i - 2))
        return memo[i]

    return dp(len(nums) - 1)


def rob_tab(nums):
    """
    House Robber using Bottom-Up Tabulation.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[-1]


if __name__ == "__main__":
    import unittest

    class TestHouseRobber(unittest.TestCase):
        def test_house_robber(self):
            self.assertEqual(rob([1, 2, 3, 1]), 4)
            self.assertEqual(rob([2, 7, 9, 3, 1]), 12)
            self.assertEqual(rob([2, 1, 1, 2]), 4)
            self.assertEqual(rob([1]), 1)
            self.assertEqual(rob([]), 0)

        def test_house_robber_memo(self):
            self.assertEqual(rob_memo([1, 2, 3, 1]), 4)
            self.assertEqual(rob_memo([2, 7, 9, 3, 1]), 12)

        def test_house_robber_tab(self):
            self.assertEqual(rob_tab([1, 2, 3, 1]), 4)
            self.assertEqual(rob_tab([2, 7, 9, 3, 1]), 12)

    # Demo
    demo = [2, 7, 9, 3, 1]
    print(f"Houses: {demo}")
    print(f"Maximum amount we can rob: {rob(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)