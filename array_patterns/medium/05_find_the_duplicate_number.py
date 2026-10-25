# 📘 Array Patterns — Medium 05
# Topic: Hashing / Floyd's Cycle Detection — Find the Duplicate Number
# Approach: Floyd's Tortoise and Hare (O(1) space) or hashmap
# Time: O(n) | Space: O(1)

def find_duplicate(arr):
    """
    Finds the duplicate number in array [1..n] with n+1 elements.
    Uses Floyd's Cycle Detection (O(1) space).
    """
    # Phase 1: Find intersection point
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    # Phase 2: Find the entrance to cycle (the duplicate)
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow


def find_duplicate_hash(arr):
    """
    Hashmap approach — O(n) time, O(n) space.
    """
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1


def find_duplicate_sort(arr):
    """
    Sort approach — O(n log n) time, O(1) space.
    """
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return arr[i]
    return -1


if __name__ == "__main__":
    import unittest

    class TestFindDuplicate(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(find_duplicate([1, 3, 4, 2, 2]), 2)

        def test_duplicates(self):
            self.assertEqual(find_duplicate([3, 1, 3, 4, 2]), 3)

        def test_duplicate_at_end(self):
            self.assertEqual(find_duplicate([3, 1, 3, 4, 2]), 3)

    # Demo
    demo = [1, 3, 4, 2, 2]
    print(f"Input: {demo}")
    print(f"Duplicate: {find_duplicate(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
