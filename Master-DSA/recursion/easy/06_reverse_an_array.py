# 📘 Recursion — Easy 06
# Topic: Array Recursion — Reverse an Array
# Approach: Two-pointer recursion
# Time: O(n) | Space: O(n) (call stack)

def reverse_array(arr):
    """
    Reverses an array in-place using recursion.
    """
    def reverse(left, right):
        if left >= right:
            return arr
        arr[left], arr[right] = arr[right], arr[left]
        return reverse(left + 1, right - 1)

    return reverse(0, len(arr) - 1)


def reverse_array_recursive(arr, left=0, right=None):
    """
    Reverses an array in-place using recursion.
    With explicit left/right parameters.
    """
    if right is None:
        right = len(arr) - 1
    if left >= right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    return reverse_array_recursive(arr, left + 1, right - 1)


def reverse_array_brute(arr):
    """
    Reverses an array using brute force (built-in reverse).
    """
    return arr[::-1]


if __name__ == "__main__":
    import unittest

    class TestReverseArray(unittest.TestCase):
        def test_basic(self):
            arr = [1, 2, 3, 4, 5]
            reverse_array(arr)
            self.assertEqual(arr, [5, 4, 3, 2, 1])

        def test_even_length(self):
            arr = [1, 2, 3, 4]
            reverse_array(arr)
            self.assertEqual(arr, [4, 3, 2, 1])

        def test_single(self):
            arr = [1]
            reverse_array(arr)
            self.assertEqual(arr, [1])

        def test_empty(self):
            arr = []
            reverse_array(arr)
            self.assertEqual(arr, [])

    # Demo
    demo = [1, 2, 3, 4, 5]
    print(f"Input: {demo}")
    print(f"Reversed: {reverse_array(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
