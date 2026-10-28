# 📘 Binary Search — Advanced Easy 02
# Topic: Count Occurrences in Sorted Array
# Approach: Binary search for first and last occurrence
# Time: O(log n) | Space: O(1)

def count_occurrences(nums, target):
    """
    Returns the count of occurrences of target in sorted array.
    Uses binary search to find first and last position.
    """
    def find_first(nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left if left < len(nums) and nums[left] == target else -1

    def find_last(nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left - 1 if left > 0 and nums[left - 1] == target else -1

    first = find_first(nums, target)
    if first == -1:
        return 0
    last = find_last(nums, target)
    return last - first + 1


def count_occurrences_brute(nums, target):
    """
    Brute force: O(n) linear scan.
    """
    return sum(1 for num in nums if num == target)


if __name__ == "__main__":
    import unittest

    class TestCountOccurrences(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(count_occurrences([1, 1, 2, 2, 2, 2, 3], 2), 4)

        def test_not_present(self):
            self.assertEqual(count_occurrences([1, 2, 3, 4, 5], 6), 0)

        def test_all_same(self):
            self.assertEqual(count_occurrences([5, 5, 5, 5], 5), 4)

        def test_single(self):
            self.assertEqual(count_occurrences([1], 1), 1)

    # Demo
    demo = [1, 1, 2, 2, 2, 2, 3]
    target = 2
    print(f"Input: {demo}, target = {target}")
    print(f"Count: {count_occurrences(demo, target)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
