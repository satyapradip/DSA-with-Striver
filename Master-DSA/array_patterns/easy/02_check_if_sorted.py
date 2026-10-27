# 📘 Array Patterns — Easy 02
# Topic: Traversal & Basic Ops — Check if Array is Sorted
# Approach: Single pass, compare adjacent elements
# Time: O(n) | Space: O(1)

def is_sorted(arr):
    """
    Returns True if array is sorted in non-decreasing order.
    """
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def is_sorted_descending(arr):
    """
    Returns True if array is sorted in non-increasing order.
    """
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False
    return True


if __name__ == "__main__":
    import unittest

    class TestIsSorted(unittest.TestCase):
        def test_sorted(self):
            self.assertTrue(is_sorted([1, 2, 3, 4, 5]))

        def test_unsorted(self):
            self.assertFalse(is_sorted([1, 3, 2, 4]))

        def test_empty(self):
            self.assertTrue(is_sorted([]))

    # Demo
    demo = [1, 2, 3, 4, 5]
    print(f"Input: {demo}")
    print(f"Sorted? {is_sorted(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
