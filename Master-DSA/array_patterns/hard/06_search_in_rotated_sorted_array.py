# 📘 Array Patterns — Hard 06
# Topic: Binary Search — Search in Rotated Sorted Array
# Approach: Modified binary search (O(log n) time, O(1) space)
# Note: Array is sorted and rotated. Find target index.

def search_rotated(nums, target):
    """
    Returns the index of target in a rotated sorted array.
    If not found, returns -1.
    """
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


def search_rotated_brute(nums, target):
    """
    Brute force: O(n) linear search.
    """
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


if __name__ == "__main__":
    import unittest

    class TestSearchRotated(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 0), 4)

        def test_not_found(self):
            self.assertEqual(search_rotated([4, 5, 6, 7, 0, 1, 2], 3), -1)

        def test_single_element(self):
            self.assertEqual(search_rotated([1], 1), 0)

    # Demo
    demo = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(f"Array: {demo}, target: {target}")
    print(f"Index: {search_rotated(demo, target)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
