# 📘 Linked List (Easy 09)
# Topic: Check if Linked List is a Palindrome
# Approach: Find middle → Reverse second half → Compare
# Time: O(n) | Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head):
    """
    Check if a linked list is a palindrome.
    """
    if not head or not head.next:
        return True

    # Find middle - use fast = head.next so first half includes the middle for even-length lists
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    second = slow.next
    slow.next = None
    prev = None
    while second:
        next_node = second.next
        second.next = prev
        prev = second
        second = next_node

    # Compare first half and reversed second half
    first = head
    second = prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True


def is_palindrome_brute(head):
    """
    Brute force: O(n) space, O(n) time.
    Collect values in array, then check if array is palindrome.
    """
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next

    left = 0
    right = len(values) - 1
    while left < right:
        if values[left] != values[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    import unittest

    class TestIsPalindrome(unittest.TestCase):
        def test_is_palindrome_true(self):
            head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
            self.assertTrue(is_palindrome(head))

        def test_is_palindrome_false(self):
            head = ListNode(1, ListNode(2))
            self.assertFalse(is_palindrome(head))

        def test_is_palindrome_single(self):
            head = ListNode(1)
            self.assertTrue(is_palindrome(head))

        def test_is_palindrome_brute(self):
            self.assertTrue(is_palindrome_brute(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
            self.assertFalse(is_palindrome_brute(ListNode(1, ListNode(2))))

    # Demo
    demo = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(f"Is palindrome? {is_palindrome(demo)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)