# 📘 Recursion — Easy 01
# Topic: Basic Recursion — Print a Name N Times
# Approach: Simple recursion with counter
# Time: O(n) | Space: O(n) (call stack)

def print_name_n_times(name, n):
    """
    Prints the given name n times using recursion.
    """
    if n <= 0:
        return
    print(name)
    print_name_n_times(name, n - 1)


def print_name_n_times_optimized(name, n, current=1):
    """
    Prints the given name n times using recursion.
    Uses an additional parameter to track the current count.
    """
    if current > n:
        return
    print(name)
    print_name_n_times_optimized(name, n, current + 1)


if __name__ == "__main__":
    import unittest

    class TestPrintNameNTimes(unittest.TestCase):
        def test_basic(self):
            # Capture output
            import io
            from contextlib import redirect_stdout
            buf = io.StringIO()
            with redirect_stdout(buf):
                print_name_n_times("Alice", 3)
            output = buf.getvalue().strip().split('\n')
            self.assertEqual(output, ["Alice", "Alice", "Alice"])

    # Demo
    demo_name = "Alice"
    demo_n = 3
    print(f"Printing '{demo_name}' {demo_n} times:")
    print_name_n_times(demo_name, demo_n)
    print("Running unit tests...")
    unittest.main(verbosity=0)
