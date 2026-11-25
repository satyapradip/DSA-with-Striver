# 📘 Greedy Algorithms (Easy 04)
# Topic: Monotonic Array
# Approach: Check if array is entirely non-increasing or non-decreasing
# Time: O(n) | Space: O(1)

def is_monotonic(nums):
    """
    Check if array is monotonic (entirely non-increasing or non-decreasing).
    """
    increasing = True
    decreasing = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False

    return increasing or decreasing


def is_monotonic_brute(nums):
    """
    Brute force: Check all possible monotonic patterns.
    """
    if len(nums) <= 2:
        return True

    # Check non-decreasing
    non_decreasing = all(nums[i] >= nums[i - 1] for i in range(1, len(nums)))
    if non_decreasing:
        return True

    # Check non-increasing
    non_increasing = all(nums[i] <= nums[i - 1] for i in range(1, len(nums)))
    return non_increasing


if __name__ == "__main__":
    import unittest

    class TestMonotonicArray(unittest.TestCase):
        def test_monotonic_increasing(self):
            self.assertTrue(is_monotonic([1, 2, 2, 3]))

        def test_monotonic_decreasing(self):
            self.assertTrue(is_monotonic([6, 5, 4, 4]))

        def test_not_monotonic(self):
            self.assertFalse(is_monotonic([1, 3, 2]))

        def test_single_element(self):
            self.assertTrue(is_monotonic([1]))

        def test_two_elements(self):
            self.assertTrue(is_monotonic([2, 1]))
            self.assertTrue(is_monotonic([1, 2]))

    # Demo
    demo = [1, 2, 2, 3]
    print(f"Array: {demo}")
    print(f"Is monotonic? {is_monotonic(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)