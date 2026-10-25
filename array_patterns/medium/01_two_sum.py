# 📘 Array Patterns — Medium 01
# Topic: Two Pointers / Hashing — Two Sum
# Approach: Hashmap (optimal for unsorted), Two pointers (sorted)
# Time (opt): O(n) | Space: O(n)
# Note: Two pointers only works on sorted arrays

def two_sum(nums, target):
    """
    Find two numbers that add up to target.
    Returns indices of the two numbers (original array order).
    Uses hashmap for O(n) optimal solution.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


def two_sum_two_pointers(nums, target):
    """
    Two pointers approach — ONLY works on sorted arrays.
    Returns indices in sorted array, not original.
    """
    nums_sorted = sorted(enumerate(nums), key=lambda x: x[1])
    left, right = 0, len(nums_sorted) - 1
    while left < right:
        current = nums_sorted[left][1] + nums_sorted[right][1]
        if current == target:
            return [nums_sorted[left][0], nums_sorted[right][0]]
        elif current < target:
            left += 1
        else:
            right -= 1
    return []


def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


if __name__ == "__main__":
    import unittest

    class TestTwoSum(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

        def test_no_match(self):
            self.assertEqual(two_sum([1, 2, 3], 7), [])

        def test_two_pointers_sorted(self):
            # works on sorted array
            self.assertEqual(two_sum_two_pointers([2, 7, 11, 15], 9), [0, 1])

    # Demo
    demo = [2, 7, 11, 15]
    target = 9
    print(f"Input: {demo}, target = {target}")
    print(f"Two Sum: {two_sum(demo, target)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
