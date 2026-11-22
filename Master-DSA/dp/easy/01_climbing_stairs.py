# 📘 Dynamic Programming (DP) — Easy 01
# Topic: 1D DP — Climbing Stairs
# Approach: 1D DP (memoization + tabulation)
# Time: O(n) | Space: O(n) [O(1) optimized]

def climb_stairs_memo(n, memo=None):
    """
    Climbing Stairs using Top-Down Memoization.
    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    if n <= 2:
        return n

    memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]


def climb_stairs_tab(n):
    """
    Climbing Stairs using Bottom-Up Tabulation.
    """
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climb_stairs_optimized(n):
    """
    Climbing Stairs using constant space (optimized).
    """
    if n <= 2:
        return n

    prev2 = 1  # dp[i-2]
    prev1 = 2  # dp[i-1]

    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


def climb_stairs_matrix_exponentiation(n):
    """
    Climbing Stairs using Matrix Exponentiation (O(log n)).
    Based on Fibonacci formula: F(n) = [[1,1],[1,0]]^(n-1) * [1,0]
    """
    if n <= 2:
        return n

    def multiply(A, B):
        """Multiply two 2x2 matrices."""
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]

    def power(matrix, exp):
        """Fast exponentiation for matrix."""
        result = [[1, 0], [0, 1]]  # Identity matrix
        while exp > 0:
            if exp % 2 == 1:
                result = multiply(result, matrix)
            matrix = multiply(matrix, matrix)
            exp //= 2
        return result

    base = [[1, 1], [1, 0]]
    result = power(base, n - 1)
    return result[0][0]


if __name__ == "__main__":
    import unittest

    class TestClimbingStairs(unittest.TestCase):
        def test_climbing_stairs(self):
            self.assertEqual(climb_stairs_memo(2), 2)
            self.assertEqual(climb_stairs_memo(3), 3)
            self.assertEqual(climb_stairs_memo(4), 5)
            self.assertEqual(climb_stairs_memo(5), 8)
            self.assertEqual(climb_stairs_memo(10), 89)

        def test_climbing_stairs_tab(self):
            self.assertEqual(climb_stairs_tab(2), 2)
            self.assertEqual(climb_stairs_tab(3), 3)
            self.assertEqual(climb_stairs_tab(4), 5)
            self.assertEqual(climb_stairs_tab(5), 8)
            self.assertEqual(climb_stairs_tab(10), 89)

        def test_climbing_stairs_optimized(self):
            self.assertEqual(climb_stairs_optimized(2), 2)
            self.assertEqual(climb_stairs_optimized(3), 3)
            self.assertEqual(climb_stairs_optimized(4), 5)
            self.assertEqual(climb_stairs_optimized(5), 8)
            self.assertEqual(climb_stairs_optimized(10), 89)

    # Demo
    n = 5
    print(f"Climbing Stairs: n={n}")
    print(f"Memoization: {climb_stairs_memo(n)}")
    print(f"Tabulation: {climb_stairs_tab(n)}")
    print(f"Optimized (O(1) space): {climb_stairs_optimized(n)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)