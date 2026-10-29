# 📘 Recursion — Easy 05
# Topic: Basic Recursion — Factorial
# Approach: Recursive product
# Time: O(n) | Space: O(n) (call stack)

def factorial(n):
    """
    Returns n! (n factorial) using recursion.
    n! = n * (n-1) * (n-2) * ... * 1
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def factorial_iterative(n):
    """
    Returns n! using iterative approach.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive_with_start(n, current=None, result=1):
    """
    Returns n! using recursion with accumulator.
    """
    if current is None:
        current = n
    if current <= 1:
        return result
    return factorial_recursive_with_start(n, current - 1, result * current)


if __name__ == "__main__":
    import unittest

    class TestFactorial(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(factorial(5), 120)  # 5*4*3*2*1

        def test_zero(self):
            self.assertEqual(factorial(0), 1)

        def test_single(self):
            self.assertEqual(factorial(1), 1)

        def test_iterative(self):
            self.assertEqual(factorial_iterative(5), 120)

    # Demo
    demo_n = 5
    print(f"Factorial of {demo_n}:")
    print(f"Recursive: {factorial(demo_n)}")
    print(f"Iterative: {factorial_iterative(demo_n)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
