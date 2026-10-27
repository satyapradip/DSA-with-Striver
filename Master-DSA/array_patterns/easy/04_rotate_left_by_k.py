# 📘 Array Patterns — Easy 04
# Topic: Traversal & Basic Ops — Rotate Array Left by K
# Approach: Temp array + modulo index
# Time: O(n) | Space: O(n)

def rotate_left_by_k(arr, k):
    """
    Rotates array to the left by k positions.
    Uses temp array approach.
    """
    n = len(arr)
    k %= n  # handle k > n
    if n == 0:
        return arr

    result = [0] * n
    for i in range(n):
        result[(i - k) % n] = arr[i]
    return result


def rotate_left_by_k_optimal(arr, k):
    """
    Optimal version using reversal technique — O(1) extra space.
    Steps: reverse(0..k-1), reverse(k..n-1), reverse(0..n-1)
    """
    n = len(arr)
    k %= n
    if n == 0 or k == 0:
        return arr

    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)
    return arr


if __name__ == "__main__":
    import unittest

    class TestRotateLeft(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(rotate_left_by_k([1, 2, 3, 4, 5], 2), [3, 4, 5, 1, 2])

        def test_k_larger_than_n(self):
            # k=7, n=5 → k=2 → [3,4,5,1,2]
            self.assertEqual(rotate_left_by_k([1, 2, 3, 4, 5], 7), [3, 4, 5, 1, 2])

        def test_k_equals_n(self):
            self.assertEqual(rotate_left_by_k([1, 2, 3], 3), [1, 2, 3])

    # Demo
    demo = [1, 2, 3, 4, 5]
    k = 2
    print(f"Input: {demo}, k = {k}")
    print(f"Rotated: {rotate_left_by_k(demo, k)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
