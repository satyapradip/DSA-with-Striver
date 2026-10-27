# 📘 Advanced Hashing — Easy 01
# Topic: Dict Hashing / Complement Lookup — Two Sum
# Approach: Hashmap (complement lookup)
# Time: O(n) | Space: O(n)

def two_sum(nums, target):
    """
    Find two numbers that add up to target.
    Returns indices of the two numbers.
    Uses complement lookup: seen[complement] = index
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def two_sum_brute(nums, target):
    """
    Brute force: O(n²) — check all pairs.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hashmap(nums, target):
    """
    Hashmap approach — O(n) time, O(n) space.
    Alternative: sorted array + two pointers (O(n log n) + O(1) space).
    """
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    for num in nums:
        complement = target - num
        if complement in freq:
            if complement == num:
                if freq[num] > 1:
                    return [nums.index(num), nums.index(num, nums.index(num) + 1)]
            else:
                return [nums.index(num), nums.index(complement)]
    return []


if __name__ == "__main__":
    import unittest

    class TestTwoSum(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

        def test_duplicate_target(self):
            self.assertEqual(two_sum([3, 3], 6), [0, 1])

        def test_no_match(self):
            self.assertEqual(two_sum([1, 2, 3], 7), [])

    # Demo
    demo = [2, 7, 11, 15]
    target = 9
    print(f"Input: {demo}, target = {target}")
    print(f"Two Sum: {two_sum(demo, target)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
