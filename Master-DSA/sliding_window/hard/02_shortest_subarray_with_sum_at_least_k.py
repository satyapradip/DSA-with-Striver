# 📘 Sliding Window — Hard 02
# Topic: Shortest Subarray with Sum at Least K (LeetCode 862)
# Approach: Prefix sum + monotonic deque
# Time: O(n) | Space: O(n)
# NOTE: NOT a simple sliding window — negatives make the window shrink logic
# create a **monotonic increasing deque** over prefix sums.

from collections import deque

def shortest_subarray_with_sum_at_least_k(nums, k):
    """
    Find length of the shortest, non-empty subarray with sum >= k.
    Uses prefix sums + monotonic increasing deque.
    Works with negatives (unlike plain sliding window).
    """
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # Deque stores indices with increasing prefix sums
    dq = deque()
    dq.append(0)   # index 0 (prefix[0] = 0)
    min_len = float('inf')

    for right in range(1, n + 1):
        # 1. Check if we can pop from left (valid subarray found)
        while dq and prefix[right] - prefix[dq[0]] >= k:
            min_len = min(min_len, right - dq.popleft())

        # 2. Maintain monotonic increasing deque:
        # pop from right while prefix[right] <= prefix[dq[-1]]
        while dq and prefix[right] <= prefix[dq[-1]]:
            dq.pop()

        dq.append(right)

    return min_len if min_len != float('inf') else -1


def shortest_subarray_with_sum_at_least_k_brute(nums, k):
    n = len(nums)
    min_len = float('inf')
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum >= k:
                min_len = min(min_len, j - i + 1)
                break
    return min_len if min_len != float('inf') else -1


if __name__ == "__main__":
    import unittest

    class TestShortestSubarraySumK(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(shortest_subarray_with_sum_at_least_k([1], 1), 1)

        def test_with_negative(self):
            self.assertEqual(shortest_subarray_with_sum_at_least_k([1, 2], 4), -1)

        def test_multiple(self):
            self.assertEqual(shortest_subarray_with_sum_at_least_k([2, -1, 2], 3), 3)

    # Demo
    demo = [1]
    k = 1
    print(f"Input: {demo}, k = {k}")
    print(f"Shortest subarray sum ≥ {k}: {shortest_subarray_with_sum_at_least_k(demo, k)} length")
    print("Running unit tests...")
    unittest.main(verbosity=0)
