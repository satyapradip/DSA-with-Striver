# 📘 Array Patterns — Hard 03
# Topic: Kadane's Algorithm — Max Subarray Sum with Indices
# Approach: Kadane's with start/end tracking
# Time: O(n) | Space: O(1)

def max_subarray_sum_with_indices(arr):
    """
    Returns (max_sum, start_index, end_index) of the maximum subarray.
    Uses Kadane's algorithm with index tracking.
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


def max_subarray_sum_with_indices_brute(arr):
    """
    Brute force: O(n³) — all subarrays.
    """
    n = len(arr)
    max_sum = float('-inf')
    start = end = 0
    for i in range(n):
        for j in range(i, n):
            current_sum = sum(arr[i:j + 1])
            if current_sum > max_sum:
                max_sum = current_sum
                start, end = i, j
    return max_sum, start, end


if __name__ == "__main__":
    import unittest

    class TestMaxSubarrayIndices(unittest.TestCase):
        def test_basic(self):
            result = max_subarray_sum_with_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
            self.assertEqual(result, (6, 3, 6))

        def test_all_negative(self):
            result = max_subarray_sum_with_indices([-5, -2, -9, -1])
            self.assertEqual(result, (-1, 3, 3))

    # Demo
    demo = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, s, e = max_subarray_sum_with_indices(demo)
    print(f"Input: {demo}")
    print(f"Max subarray sum: {max_sum}")
    print(f"Subarray: {demo[s:e+1]} (indices {s}..{e})")
    print("Running unit tests...")
    unittest.main(verbosity=0)
