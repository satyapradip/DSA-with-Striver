# 📘 Array Patterns — Medium 07
# Topic: Kadane's Algorithm — Maximum Subarray Sum
# Approach: Kadane's (dynamic programming on array)
# Time: O(n) | Space: O(1)

def max_subarray_sum(arr):
    """
    Returns the maximum sum of any contiguous subarray.
    Uses Kadane's Algorithm.
    """
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_subarray_sum_brute(arr):
    """
    Brute force: all subarrays + sum.
    """
    n = len(arr)
    max_sum = float('-inf')
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
    return max_sum


def max_subarray_sum_kadane_with_indices(arr):
    """
    Kadane's with start/end indices tracking.
    """
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    temp_start = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return max_sum, start, end


if __name__ == "__main__":
    import unittest

    class TestMaxSubarraySum(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

        def test_all_negative(self):
            self.assertEqual(max_subarray_sum([-2, -3, -1, -5]), -1)

        def test_all_positive(self):
            self.assertEqual(max_subarray_sum([1, 2, 3, 4]), 10)

    # Demo
    demo = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Input: {demo}")
    print(f"Max subarray sum: {max_subarray_sum(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
