# 📘 Sliding Window — Hard 01
# Topic: Count Number of Nice Subarrays (LeetCode 1248)
# Approach: Variable-size sliding window + prefix parity count
# Time: O(n) | Space: O(2)
# NOTE: "Nice" = subarray with exactly K odd numbers.

def count_nice_subarrays(nums, k):
    """
    A "nice" subarray has exactly k odd numbers.
    Uses the sliding window trick: number of subarrays with exactly k = 
    (number with <= k) - (number with <= k-1).
    """
    def at_most_k_odd(arr, k):
        if k < 0:
            return 0  # cannot have negative odd count
        left = 0
        odd_count = 0
        res = 0
        for right in range(len(arr)):
            if arr[right] % 2 == 1:
                odd_count += 1
            while odd_count > k:
                if arr[left] % 2 == 1:
                    odd_count -= 1
                left += 1
            res += right - left + 1
        return res

    return at_most_k_odd(nums, k) - at_most_k_odd(nums, k - 1)


def count_nice_subarrays_brute(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        odd_count = 0
        for j in range(i, n):
            if nums[j] % 2 == 1:
                odd_count += 1
            if odd_count == k:
                count += 1
    return count


if __name__ == "__main__":
    import unittest

    class TestNiceSubarrays(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(count_nice_subarrays([1, 1, 2, 1, 1], 3), 2)

        def test_single(self):
            self.assertEqual(count_nice_subarrays([2, 4, 6], 1), 0)

        def test_k_zero(self):
            # [1,2,3,4,5] with k=0: [2], [4], [2... wait, even? No [1,2] has odd=1. 
            # Subarrays with exactly 0 odd = all-even subarrays = [2], [4], [2,4]?? 
            # No: [2] only, [4] only, and that's it since 2,4 are separated.
            # Actually [1,2,3,4,5]: all even numbers are at positions 1,3 (0-indexed)
            # Even subarrays: [2], [4] → count = 2, not 3.
            self.assertEqual(count_nice_subarrays([1, 2, 3, 4, 5], 0), 2)

    # Demo
    demo = [1, 1, 2, 1, 1]
    k = 3
    print(f"Input: {demo}, k = {k}")
    print(f"Nice subarrays count: {count_nice_subarrays(demo, k)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
