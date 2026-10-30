# 📘 Linked List — Medium 03
# Topic: Fast & Slow Pointers — Palindrome Linked List
# Approach: Find middle, reverse second half, compare
# Time: O(n) | Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def is_palindrome(head):
    """
    Returns True if the linked list is a palindrome.
    Uses O(1) extra space.
    """
    if not head or not head.next:
        return True

    # Step 1: Find the middle using fast/slow pointers
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    second_half = slow.next
    slow.next = None  # Break the list
    prev = None
    current = second_half
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    second_half = prev

    # Step 3: Compare first half with reversed second half
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


def is_palindrome_brute(head):
    """
    Checks if the linked list is a palindrome using O(n) extra space.
    """
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values == values[::-1]


if __name__ == "__main__":
    import unittest

    class TestPalindromeLL(unittest.TestCase):
        def test_palindrome(self):
            head = create_linked_list([1, 2, 3, 2, 1])
            self.assertTrue(is_palindrome(head))

        def test_not_palindrome(self):
            head = create_linked_list([1, 2, 3, 4, 5])
            self.assertFalse(is_palindrome(head))

        def test_single_node(self):
            head = create_linked_list([1])
            self.assertTrue(is_palindrome(head))

        def test_empty(self):
            head = create_linked_list([])
            self.assertTrue(is_palindrome(head))

        def test_even_palindrome(self):
            head = create_linked_list([1, 2, 2, 1])
            self.assertTrue(is_palindrome(head))

    # Demo
    demo = [1, 2, 3, 2, 1]
    head = create_linked_list(demo)
    print(f"Linked List: {linked_list_to_array(head)}")
    print(f"Is palindrome: {is_palindrome(head)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
