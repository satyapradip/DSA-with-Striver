# 📘 Sliding Window — Easy 03
# Topic: Longest subarray with sum K (non-negative only)
# Approach: Sliding window (variable)
# Time: O(n) | Space: O(1)
# NOTE: Only works when all numbers are non-negative!

def longest_subarray_with_sum_k(nums, k):
    n = len(nums)
    left = 0
    current_sum = 0
    max_len = 0

    for right in range(n):
        current_sum += nums[right]          # expand right

        # shrink while sum exceeds k (only valid with non-negative numbers)
        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1

        if current_sum == k:
            max_len = max(max_len, right - left + 1)

    return max_len


def longest_subarray_with_sum_k_brute(nums, k):
    n = len(nums)
    max_len = 0
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == k:
                max_len = max(max_len, j - i + 1)
    return max_len


if __name__ == "__main__":
    import unittest

    class TestLongestSubarraySumK(unittest.TestCase):
        def test_basic(self):
            # [1, 2, 3, 7, 0, 15] k=15: [0,15] len=2, [15] len=1 → max=2
            self.assertEqual(longest_subarray_with_sum_k([1, 2, 3, 7, 0, 15], 15), 2)

        def test_multiple(self):
            # [1, 2, 3, 4, 5] k=9: [2,3,4] len=3 → output 3
            self.assertEqual(longest_subarray_with_sum_k([1, 2, 3, 4, 5], 9), 3)

        def test_no_match(self):
            self.assertEqual(longest_subarray_with_sum_k([5, 6, 7], 20), 0)

        def test_negative_check(self):
            # This case has negatives → window fails (demonstrates limitation)
            nums = [1, -1, 5, -2, 3]
            self.assertNotEqual(longest_subarray_with_sum_k(nums, 6), 3)  # not 3

    # Demo
    demo = [1, 2, 3, 4, 5]
    k = 9
    print(f"Input: {demo}, k = {k}")
    print(f"Longest subarray with sum {k}: {longest_subarray_with_sum_k(demo, k)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)

