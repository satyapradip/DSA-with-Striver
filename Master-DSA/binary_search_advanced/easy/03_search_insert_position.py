# 📘 Binary Search — Advanced Easy 03
# Topic: Search Insert Position (Half-Open Binary Search)
# Approach: Binary search for insertion position
# Time: O(log n) | Space: O(1)

def search_insert_position(nums, target):
    """
    Returns the index where target should be inserted to maintain sorted order.
    If target is already present, returns its index.
    """
    left, right = 0, len(nums)  # half-open: [0, n)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left


def search_insert_position_brute(nums, target):
    """
    Brute force: O(n) linear search.
    """
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)


if __name__ == "__main__":
    import unittest

    class TestSearchInsertPosition(unittest.TestCase):
        def test_present(self):
            self.assertEqual(search_insert_position([1, 3, 5, 6], 5), 2)

        def test_not_present(self):
            self.assertEqual(search_insert_position([1, 3, 5, 6], 2), 1)

        def test_greater_than_all(self):
            self.assertEqual(search_insert_position([1, 3, 5, 6], 7), 4)

        def test_less_than_all(self):
            self.assertEqual(search_insert_position([1, 3, 5, 6], 0), 0)

    # Demo
    demo = [1, 3, 5, 6]
    target = 5
    print(f"Input: {demo}, target = {target}")
    print(f"Insert position: {search_insert_position(demo, target)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
