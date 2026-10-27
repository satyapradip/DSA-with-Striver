# 📘 Sliding Window — Easy 01
# Topic: Max Consecutive Ones (LeetCode 485)
# Approach: Fixed/Variable sliding window
# Time: O(n) | Space: O(1)

def max_consecutive_ones(nums):
    n = len(nums)
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count


if __name__ == "__main__":
    import unittest

    class TestMaxConsecutiveOnes(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(max_consecutive_ones([1, 1, 0, 1, 1, 1]), 3)

        def test_all_ones(self):
            self.assertEqual(max_consecutive_ones([1, 1, 1, 1]), 4)

        def test_all_zeros(self):
            self.assertEqual(max_consecutive_ones([0, 0, 0]), 0)

        def test_single(self):
            self.assertEqual(max_consecutive_ones([1]), 1)

    # Run demo
    demo = [1, 1, 0, 1, 1, 1, 0, 1, 1]
    print(f"Input: {demo}")
    print(f"Output: {max_consecutive_ones(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
