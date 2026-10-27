# 📘 Sliding Window — Easy 02
# Topic: Max subarray sum of fixed size K (LeetCode 209 variant / GFG)
# Approach: Sliding window (fixed-size)
# Time: O(n) | Space: O(1)

def max_subarray_sum_of_size_k(nums, k):
    n = len(nums)
    if n < k:
        return None

    # sum of first window [0..k-1]
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # slide the window: remove left, add right
    for right in range(k, n):
        window_sum = window_sum - nums[right - k] + nums[right]
        max_sum = max(max_sum, window_sum)

    return max_sum


def max_subarray_sum_of_size_k_brute(nums, k):
    n = len(nums)
    max_sum = float('-inf')
    for i in range(n - k + 1):
        current_sum = sum(nums[i:i + k])
        max_sum = max(max_sum, current_sum)
    return max_sum


if __name__ == "__main__":
    import unittest

    class TestMaxSubarraySumSizeK(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(max_subarray_sum_of_size_k([2, 1, 5, 1, 3, 2], 3), 9)

        def test_k_equals_n(self):
            self.assertEqual(max_subarray_sum_of_size_k([1, 4, 2, 10, 23, 3, 1, 0, 20], 4), 39)

        def test_negatives(self):
            self.assertEqual(max_subarray_sum_of_size_k([-1, -2, -3, -4], 2), -3)

    # Demo
    demo = [2, 1, 5, 1, 3, 2]
    k = 3
    print(f"Input: {demo}, k = {k}")
    print(f"Max subarray sum of size {k}: {max_subarray_sum_of_size_k(demo, k)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
