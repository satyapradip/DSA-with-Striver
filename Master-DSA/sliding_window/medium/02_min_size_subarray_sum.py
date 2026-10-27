# 📘 Sliding Window — Medium 02
# Topic: Minimum Size Subarray Sum (LeetCode 209)
# Approach: Variable-size sliding window
# Time: O(n) | Space: O(1)
# NOTE: Works with non-negative numbers only.

def min_subarray_length(nums, target):
    n = len(nums)
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(n):
        current_sum += nums[right]          # expand right

        # shrink while sum >= target
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]       # shrink left
            left += 1

    return min_len if min_len != float('inf') else 0


def min_subarray_length_brute(nums, target):
    n = len(nums)
    min_len = float('inf')
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum >= target:
                min_len = min(min_len, j - i + 1)
    return min_len if min_len != float('inf') else 0


if __name__ == "__main__":
    import unittest

    class TestMinSubarrayLength(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(min_subarray_length([2, 3, 1, 2, 4, 3], 7), 2)

        def test_single_element(self):
            self.assertEqual(min_subarray_length([1, 2, 3], 3), 1)

        def test_no_match(self):
            self.assertEqual(min_subarray_length([1, 1, 1], 10), 0)

    # Demo
    demo = [2, 3, 1, 2, 4, 3]
    target = 7
    print(f"Input: {demo}, target = {target}")
    print(f"Min subarray length: {min_subarray_length(demo, target)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
