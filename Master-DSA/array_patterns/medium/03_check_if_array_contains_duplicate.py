# 📘 Array Patterns — Medium 03
# Topic: Hashing — Contains Duplicate
# Approach: Frequency map (or sorting or set)
# Time: O(n) | Space: O(n)

def contains_duplicate(nums):
    """
    Returns True if any value appears at least twice.
    Uses set (most optimal: O(n) time).
    """
    return len(nums) != len(set(nums))


def contains_duplicate_frequency(nums):
    """
    Frequency map approach (more informative: shows count).
    """
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return any(count > 1 for count in freq.values())


def contains_duplicate_sort(nums):
    """
    Sort approach — O(n log n) time, O(1) space (if in-place sort allowed).
    """
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


if __name__ == "__main__":
    import unittest

    class TestContainsDuplicate(unittest.TestCase):
        def test_basic(self):
            self.assertTrue(contains_duplicate([1, 2, 3, 1]))

        def test_no_duplicate(self):
            self.assertFalse(contains_duplicate([1, 2, 3, 4]))

        def test_all_same(self):
            self.assertTrue(contains_duplicate([3, 3, 3]))

    # Demo
    demo = [1, 2, 3, 1]
    print(f"Input: {demo}")
    print(f"Contains duplicate? {contains_duplicate(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
