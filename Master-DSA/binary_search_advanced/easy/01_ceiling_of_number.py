# 📘 Binary Search — Advanced Easy 01
# Topic: Ceiling of a Number (Half-Open Binary Search)
# Approach: Binary search to find smallest element >= target
# Time: O(log n) | Space: O(1)

def ceiling_of_number(nums, target):
    """
    Returns the smallest element in sorted array that is >= target.
    If all elements are smaller, returns -1.
    """
    n = len(nums)
    left, right = 0, n  # half-open: [0, n)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return nums[left] if left < n else -1


def ceiling_of_number_brute(nums, target):
    """
    Brute force: O(n) linear search.
    """
    for num in nums:
        if num >= target:
            return num
    return -1


if __name__ == "__main__":
    import unittest

    class TestCeilingOfNumber(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(ceiling_of_number([1, 3, 8, 10, 15], 8), 8)

        def test_not_present(self):
            self.assertEqual(ceiling_of_number([1, 3, 8, 10, 15], 12), 15)

        def test_everything_smaller(self):
            self.assertEqual(ceiling_of_number([1, 3, 8], 20), -1)

        def test_equal(self):
            self.assertEqual(ceiling_of_number([1, 3, 8, 10], 3), 3)

    # Demo
    demo = [1, 3, 8, 10, 15]
    target = 8
    print(f"Input: {demo}, target = {target}")
    print(f"Celing: {ceiling_of_number(demo, target)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
