# 📘 Recursion — Easy 02
# Topic: Basic Recursion — Print 1 to N
# Approach: Forward recursion (increment until base case)
# Time: O(n) | Space: O(n) (call stack)

def print_1_to_n(n):
    """
    Prints numbers from 1 to n using recursion.
    """
    if n <= 0:
        return
    print_1_to_n(n - 1)
    print(n)


def print_1_to_n_optimized(n, current=1):
    """
    Prints numbers from 1 to n using recursion.
    Uses an additional parameter for the current counter.
    """
    if current > n:
        return
    print(current)
    print_1_to_n_optimized(n, current + 1)


def print_1_to_n_reverse(n):
    """
    Prints numbers from n down to 1 using recursion.
    (Alternative: forward recursion but starting from n)
    """
    if n <= 0:
        return
    print(n)
    print_1_to_n_reverse(n - 1)


if __name__ == "__main__":
    import unittest

    class TestPrint1ToN(unittest.TestCase):
        def test_basic(self):
            import io
            from contextlib import redirect_stdout
            buf = io.StringIO()
            with redirect_stdout(buf):
                print_1_to_n(5)
            output = buf.getvalue().strip().split('\n')
            self.assertEqual(output, ["1", "2", "3", "4", "5"])

    # Demo
    demo_n = 5
    print(f"Printing 1 to {demo_n}:")
    print_1_to_n(demo_n)
    print("Running unit tests...")
    unittest.main(verbosity=0)
