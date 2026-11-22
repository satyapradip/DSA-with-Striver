# 📘 Dynamic Programming (DP) — Easy 03
# Topic: 1D DP — Maximum Subarray Sum (Kadane's Algorithm)
# Approach: 1D DP
# Time: O(n) | Space: O(1)

def max_subarray_sum(nums):
    """
    Maximum Subarray Sum using Kadane's Algorithm.
    Returns the maximum sum of a contiguous subarray.
    """
    if not nums:
        return 0

    max_so_far = nums[0]
    max_ending_here = nums[0]

    for i in range(1, len(nums)):
        # Either extend current subarray or start new one
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def max_subarray_sum_indices(nums):
    """
    Maximum Subarray Sum returning the actual subarray.
    """
    if not nums:
        return [], 0

    max_so_far = nums[0]
    max_ending_here = nums[0]
    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(nums)):
        if nums[i] > max_ending_here + nums[i]:
            # Start new subarray
            max_ending_here = nums[i]
            temp_start = i
        else:
            # Extend current subarray
            max_ending_here = max_ending_here + nums[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i

    return nums[start:end + 1], max_so_far


def max_subarray_sum_memo(nums):
    """
    Maximum Subarray Sum using Top-Down Memoization.
    dp[i] = maximum subarray sum ending at index i
    """
    if not nums:
        return 0

    memo = {}

    def dp(i):
        if i in memo:
            return memo[i]
        if i == 0:
            return nums[0]

        # Either extend current subarray or start new one at i
        memo[i] = max(nums[i], nums[i] + dp(i - 1))
        return memo[i]

    # The answer is the max of all dp[i] values
    max_sum = nums[0]
    for i in range(len(nums)):
        max_sum = max(max_sum, dp(i))

    return max_sum


if __name__ == "__main__":
    import unittest

    class TestMaximumSubarraySum(unittest.TestCase):
        def test_max_subarray_sum(self):
            self.assertEqual(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
            self.assertEqual(max_subarray_sum([-2, -1]), -1)
            self.assertEqual(max_subarray_sum([1]), 1)
            self.assertEqual(max_subarray_sum([5, 4, -1, 7, 8]), 23)

        def test_max_subarray_sum_indices(self):
            arr, max_sum = max_subarray_sum_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
            self.assertEqual(arr, [4, -1, 2, 1])
            self.assertEqual(max_sum, 6)

        def test_max_subarray_sum_memo(self):
            self.assertEqual(max_subarray_sum_memo([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
            self.assertEqual(max_subarray_sum_memo([-2, -1]), -1)

    # Demo
    demo = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Array: {demo}")
    print(f"Maximum subarray sum: {max_subarray_sum(demo)}")
    sub_arr, max_sum = max_subarray_sum_indices(demo)
    print(f"Subarray: {sub_arr}, Sum: {max_sum}")
    print("Running unit tests...")
    unittest.main(verbosity=0)