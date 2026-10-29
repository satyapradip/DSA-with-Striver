# 📘 Recursion — Easy 03
# Topic: Basic Recursion — Print N to 1
# Approach: Backward recursion (print then recurse)
# Time: O(n) | Space: O(n) (call stack)

def print_n_to_1(n):
    """
    Prints numbers from n down to 1 using recursion.
    """
    if n <= 0:
        return
    print(n)
    print_n_to_1(n - 1)


def print_n_to_1_optimized(n, current=None):
    """
    Prints numbers from n down to 1 using recursion.
    Uses a start parameter to control the direction.
    """
    if current is None:
        current = n
    if current <= 0:
        return
    print(current)
    print_n_to_1_optimized(n, current - 1)


def print_1_to_n_optimized(n, current=1):
    """
    Prints numbers from 1 to n using recursion.
    (Alternative version for comparison)
    """
    if current > n:
        return
    print(current)
    print_1_to_n_optimized(n, current + 1)


if __name__ == "__main__":
    import unittest

    class TestPrintNTo1(unittest.TestCase):
        def test_basic(self):
            import io
            from contextlib import redirect_stdout
            buf = io.StringIO()
            with redirect_stdout(buf):
                print_n_to_1(5)
            output = buf.getvalue().strip().split('\n')
            self.assertEqual(output, ["5", "4", "3", "2", "1"])

    # Demo
    demo_n = 5
    print(f"Printing {demo_n} to 1:")
    print_n_to_1(demo_n)
    print("Running unit tests...")
    unittest.main(verbosity=0)
