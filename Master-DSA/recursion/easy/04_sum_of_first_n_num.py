# 📘 Recursion — Easy 04
# Topic: Basic Recursion — Sum of First N Numbers
# Approach: Recursive sum
# Time: O(n) | Space: O(n) (call stack)

def sum_of_first_n(n):
    """
    Returns the sum of first n natural numbers using recursion.
    """
    if n <= 0:
        return 0
    return n + sum_of_first_n(n - 1)


def sum_of_first_n_formula(n):
    """
    Returns sum using formula n*(n+1)/2 — O(1) time.
    """
    return n * (n + 1) // 2


def sum_of_first_n_recursive_with_index(n, current=1, total=0):
    """
    Returns sum of first n natural numbers using recursion.
    With accumulator parameter.
    """
    if current > n:
        return total
    return sum_of_first_n_recursive_with_index(n, current + 1, total + current)


if __name__ == "__main__":
    import unittest

    class TestSumOfFirstN(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(sum_of_first_n(5), 15)  # 5+4+3+2+1

        def test_zero(self):
            self.assertEqual(sum_of_first_n(0), 0)

        def test_single(self):
            self.assertEqual(sum_of_first_n(1), 1)

        def test_formula(self):
            self.assertEqual(sum_of_first_n_formula(100), 5050)  # Gauss

    # Demo
    demo_n = 5
    print(f"Sum of first {demo_n} natural numbers:")
    print(f"Recursive: {sum_of_first_n(demo_n)}")
    print(f"Formula: {sum_of_first_n_formula(demo_n)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
