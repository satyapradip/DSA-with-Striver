# 📘 Array Patterns — Easy 03
# Topic: Traversal & Basic Ops — Sorted and Rotated
# Approach: Count "drops" using modulo
# Time: O(n) | Space: O(1)

def is_sorted_and_rotated(arr):
    """
    Returns True if array is sorted and then rotated.
    A sorted-rotated array has at most 1 drop (where arr[i] > arr[i+1]).
    0 drops = plain sorted (0 rotations), 1 drop = rotated once.
    """
    n = len(arr)
    if n <= 2:
        return True

    drops = 0
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:
            drops += 1
            if drops > 1:
                return False
    return True


def is_sorted_and_rotated_brute(arr):
    n = len(arr)
    for k in range(n):
        if all(arr[(i + k) % n] <= arr[(i + k + 1) % n] for i in range(n - 1)):
            return True
    return False


if __name__ == "__main__":
    import unittest

    class TestSortedRotated(unittest.TestCase):
        def test_basic(self):
            self.assertTrue(is_sorted_and_rotated([3, 4, 5, 1, 2]))

        def test_plain_sorted(self):
            self.assertTrue(is_sorted_and_rotated([1, 2, 3, 4, 5]))

        def test_not_rotated(self):
            self.assertFalse(is_sorted_and_rotated([2, 1, 3, 4]))

    # Demo
    demo = [3, 4, 5, 1, 2]
    print(f"Input: {demo}")
    print(f"Sorted and rotated? {is_sorted_and_rotated(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
