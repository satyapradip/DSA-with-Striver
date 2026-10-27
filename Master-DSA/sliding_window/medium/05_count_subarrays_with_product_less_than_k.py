# 📘 Sliding Window — Medium 05
# Topic: Count Subarrays With Product Less Than K (LeetCode 713)
# Approach: Variable-size sliding window + running product
# Time: O(n) | Space: O(1)
# NOTE: Works with positive numbers only (k >= 1). Fails with 0/negative.

def count_subarrays_product_less_than_k(nums, k):
    if k <= 1:
        return 0

    n = len(nums)
    left = 0
    product = 1
    count = 0

    for right in range(n):
        product *= nums[right]          # expand right

        # shrink while product >= k
        while product >= k:
            product //= nums[left]      # shrink left (integer division)
            left += 1

        # all subarrays ending at `right` and starting anywhere in [left..right]
        count += right - left + 1

    return count


def count_subarrays_product_less_than_k_brute(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            if product < k:
                count += 1
            else:
                break
    return count


if __name__ == "__main__":
    import unittest

    class TestCountProductSubarrays(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(count_subarrays_product_less_than_k([10, 5, 2, 6], 100), 8)

        def test_k_small(self):
            self.assertEqual(count_subarrays_product_less_than_k([1, 2, 3], 0), 0)

        def test_single(self):
            self.assertEqual(count_subarrays_product_less_than_k([1, 1, 1], 2), 6)

    # Demo
    demo = [10, 5, 2, 6]
    k = 100
    print(f"Input: {demo}, k = {k}")
    print(f"Subarrays with product < {k}: {count_subarrays_product_less_than_k(demo, k)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
