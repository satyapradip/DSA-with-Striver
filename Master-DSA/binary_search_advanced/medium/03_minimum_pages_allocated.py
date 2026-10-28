# 📘 Binary Search — Advanced Medium 03
# Topic: Binary Search on Answer — Allocate Books to Students
# Approach: Search the max pages answer
# Time: O(n log(max_pages))
# Space: O(1)

def allocate_books(nums, m):
    """
    Returns the minimum possible maximum pages allocated to a student
    such that m students can read the books in order.
    """
    def can_allocate(max_pages):
        students = 1
        current_pages = 0
        for pages in nums:
            if current_pages + pages > max_pages:
                students += 1
                current_pages = pages
                if students > m:
                    return False
            else:
                current_pages += pages
        return True

    if m > len(nums):
        return -1

    low, high = max(nums), sum(nums)
    while low < high:
        mid = (low + high) // 2
        if can_allocate(mid):
            high = mid
        else:
            low = mid + 1
    return low


def allocate_books_brute(nums, m):
    """
    Brute force: try all possible max pages from max(nums) to sum(nums).
    """
    for max_pages in range(max(nums), sum(nums) + 1):
        students = 1
        current_pages = 0
        for pages in nums:
            if current_pages + pages > max_pages:
                students += 1
                current_pages = pages
                if students > m:
                    break
            else:
                current_pages += pages
        if students <= m:
            return max_pages
    return -1


if __name__ == "__main__":
    import unittest

    class TestAllocateBooks(unittest.TestCase):
        def test_basic(self):
            self.assertEqual(allocate_books([10, 20, 30, 40], 2), 60)

        def test_equal(self):
            self.assertEqual(allocate_books([10, 20, 30, 40], 3), 40)

        def test_single(self):
            self.assertEqual(allocate_books([1, 2, 3], 3), 3)

    # Demo
    demo = [10, 20, 30, 40]
    demo_m = 2
    print(f"Books: {demo}, students: {demo_m}")
    print(f"Min max pages: {allocate_books(demo, demo_m)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
