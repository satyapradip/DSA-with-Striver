# 📘 Advanced Hashing — Easy 02
# Topic: Dict Hashing — Contains Duplicate
# Approach: Set (dict with count 1)
# Time: O(n) | Space: O(n)

def contains_duplicate(nums):
    """
    Returns True if any value appears at least twice.
    Uses set for O(1) lookup — O(n) time, O(n) space.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate_set(nums):
    """
    Set approach — O(n) time, O(n) space.
    Most Pythonic: len(nums) != len(set(nums))
    """
    return len(nums) != len(set(nums))


def contains_duplicate_sort(nums):
    """
    Sort approach — O(n log n) time, O(1) or O(n) space.
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

        def test_empty(self):
            self.assertFalse(contains_duplicate([]))

    # Demo
    demo = [1, 2, 3, 1]
    print(f"Input: {demo}")
    print(f"Contains duplicate? {contains_duplicate(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
