# 📘 Array Patterns — Easy 01
# Topic: Traversal & Basic Ops — Largest & Second Largest
# Approach: Single pass, two variables
# Time: O(n) | Space: O(1)

def largest_and_second_largest(arr):
    """
    Returns (largest, second_largest) in one pass.
    Returns None if array has < 2 distinct elements.
    """
    if len(arr) < 2:
        return None

    largest = second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num < largest:
            second = num

    return largest, second if second != float('-inf') else None


def largest_and_second_largest_brute(arr):
    if len(arr) < 2:
        return None
    arr_sorted = sorted(arr, reverse=True)
    return arr_sorted[0], arr_sorted[1]


if __name__ == "__main__":
    import unittest

    class TestLargestSecondLargest(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(largest_and_second_largest([12, 35, 1, 10, 34, 1]),
                             (35, 34))

        def test_duplicates(self):
            self.assertEqual(largest_and_second_largest([10, 10, 10]), (10, None))

        def test_two_elements(self):
            self.assertEqual(largest_and_second_largest([5, 2]), (5, 2))

    # Demo
    demo = [12, 35, 1, 10, 34, 1]
    print(f"Input: {demo}")
    print(f"Largest: {largest_and_second_largest(demo)[0]}, Second Largest: {largest_and_second_largest(demo)[1]}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
