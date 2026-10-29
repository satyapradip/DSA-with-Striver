# 📘 Recursion — Easy 07
# Topic: Basic Recursion — Fibonacci
# Approach: Recursive Fibonacci (classic)
# Time: O(2^n) | Space: O(n)
# Note: This is the naive recursive Fibonacci (very slow for large n)

def fibonacci(n):
    """
    Returns the nth Fibonacci number using recursion.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iterative(n):
    """
    Returns the nth Fibonacci number using iteration.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_memo(n, memo={}):
    """
    Returns the nth Fibonacci number using recursion + memoization.
    Time: O(n) | Space: O(n)
    """
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    import unittest

    class TestFibonacci(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(fibonacci(5), 5)   # F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5
            self.assertEqual(fibonacci(6), 8)
            self.assertEqual(fibonacci(10), 55)

        def test_zero(self):
            self.assertEqual(fibonacci(0), 0)

        def test_iterative(self):
            self.assertEqual(fibonacci_iterative(10), 55)

        def test_memo(self):
            self.assertEqual(fibonacci_memo(10), 55)

    # Demo
    demo_n = 10
    print(f"Fibonacci({demo_n}):")
    print(f"Naive recursive: {fibonacci(demo_n)}")
    print(f"Iterative: {fibonacci_iterative(demo_n)}")
    print(f"Memoized: {fibonacci_memo(demo_n)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
