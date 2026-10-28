# 📘 Binary Search — Advanced Easy 04
# Topic: Lower & Upper Bound (Half-Open Binary Search)
# Approach: Half-open binary search for first >= and first >
# Time: O(log n) | Space: O(1)

def lower_bound(nums, target):
    """
    Returns the index of the first element >= target.
    """
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left  # may be len(nums) if all elements < target


def upper_bound(nums, target):
    """
    Returns the index of the first element > target.
    """
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left  # may be len(nums) if all elements <= target


def lower_bound_brute(nums, target):
    """
    Brute force: O(n) linear search.
    """
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)


if __name__ == "__main__":
    import unittest

    class TestLowerUpperBound(unittest.TestCase):
        def test_lower_bound_basic(self):
            self.assertEqual(lower_bound([1, 2, 3, 3, 5], 3), 2)

        def test_lower_bound_not_found(self):
            self.assertEqual(lower_bound([1, 2, 3, 5], 4), 3)

        def test_lower_bound_greatest(self):
            self.assertEqual(lower_bound([1, 2, 3], 4), 3)

        def test_lower_bound_smallest(self):
            self.assertEqual(lower_bound([1, 2, 3], 0), 0)

        def test_upper_bound_basic(self):
            self.assertEqual(upper_bound([1, 2, 3, 3, 5], 3), 4)

        def test_upper_bound_not_found(self):
            self.assertEqual(upper_bound([1, 2, 3], 4), 3)

    # Demo
    demo = [1, 2, 3, 3, 5]
    target = 3
    print(f"Input: {demo}, target = {target}")
    print(f"Lower bound (first >= {target}): {lower_bound(demo, target)}")
    print(f"Upper bound (first > {target}): {upper_bound(demo, target)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
