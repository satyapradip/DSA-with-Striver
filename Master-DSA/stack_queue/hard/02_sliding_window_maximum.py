# 📘 Stacks & Queues — Hard 02
# Topic: Sliding Window / Deque — Sliding Window Maximum
# Approach: Monotonic decreasing deque
# Time: O(n) | Space: O(k)

from collections import deque

def max_sliding_window(nums, k):
    """
    Given an array nums and a sliding window of size k,
    returns the maximum values of each sliding window.
    """
    if not nums or k == 0:
        return []

    dq = deque()  # stores indices, maintaining decreasing order of values
    result = []

    for i in range(len(nums)):
        # Remove indices that are out of window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove indices with smaller values from back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add current index
        dq.append(i)

        # The front of the deque is the maximum for the current window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


def max_sliding_window_brute(nums, k):
    """
    Brute force: O(n*k) — for each window, find the max.
    """
    if not nums or k == 0:
        return []

    result = []
    for i in range(len(nums) - k + 1):
        window_max = max(nums[i:i + k])
        result.append(window_max)
    return result


if __name__ == "__main__":
    import unittest

    class TestSlidingWindowMax(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3),
                             [3, 3, 5, 5, 6, 7])

        def test_k_equals_1(self):
            self.assertEqual(max_sliding_window([1], 1), [1])

        def test_k_equals_n(self):
            self.assertEqual(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 8),
                             [7])

        def test_k_equals_2(self):
            self.assertEqual(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 2),
                             [3, 3, -1, 5, 5, 6, 7])

    # Demo
    demo_nums = [1, 3, -1, -3, 5, 3, 6, 7]
    demo_k = 3
    print(f"nums: {demo_nums}, k = {demo_k}")
    print(f"Max in each window: {max_sliding_window(demo_nums, demo_k)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
