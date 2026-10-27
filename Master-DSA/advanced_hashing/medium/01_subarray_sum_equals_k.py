# 📘 Advanced Hashing — Medium 01
# Topic: Prefix Sum + Hashmap — Subarray Sum Equals K
# Approach: Prefix sum + frequency map
# Time: O(n) | Space: O(n)
# NOTE: Only works with negatives! (sliding window fails here)

def subarray_sum_equals_k(nums, k):
    """
    Count subarrays with sum exactly k.
    Uses prefix sum + frequency hashmap.
    Works with negatives, positives, and zeros.
    """
    prefix_count = {0: 1}   # prefix sum 0 appears once (before start)
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        # if (current_sum - k) seen before, there's a subarray summing to k
        count += prefix_count.get(current_sum - k, 0)
        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

    return count


def subarray_sum_equals_k_brute(nums, k):
    """
    Brute force: O(n²) — all subarrays.
    """
    n = len(nums)
    count = 0
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == k:
                count += 1
    return count


def subarray_sum_equals_k_sliding_window(nums, k):
    """
    Sliding window — ONLY works with non-negative numbers.
    Fails with negatives (can't shrink a window with negatives).
    """
    n = len(nums)
    left = 0
    current_sum = 0
    count = 0

    for right in range(n):
        current_sum += nums[right]
        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1
        if current_sum == k:
            count += 1

    return count


if __name__ == "__main__":
    import unittest

    class TestSubarraySumK(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(subarray_sum_equals_k([1, 1, 1], 2), 2)

        def test_negatives(self):
            self.assertEqual(subarray_sum_equals_k([1, 2, -1, 2, 3], 3), 3)

        def test_zero(self):
            self.assertEqual(subarray_sum_equals_k([0, 0, 0], 0), 6)

    # Demo
    demo = [1, 1, 1]
    k = 2
    print(f"Input: {demo}, k = {k}")
    print(f"Subarrays with sum {k}: {subarray_sum_equals_k(demo, k)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
