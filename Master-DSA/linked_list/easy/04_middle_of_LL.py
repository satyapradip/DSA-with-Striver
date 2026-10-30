# 📘 Linked List — Easy 04
# Topic: Fast & Slow Pointers — Middle of Linked List
# Approach: Two pointers (slow and fast)
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


def middle_of_linked_list(head):
    """
    Returns the middle node of the linked list.
    Uses the fast/slow pointer technique.
    For even-length lists, returns the second middle node.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def middle_of_linked_list_even_length(head):
    """
    Returns the middle node for even-length lists (second middle).
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def middle_of_linked_list_first_middle(head):
    """
    Returns the first middle node for even-length lists.
    """
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    import unittest

    class TestMiddleOfLL(unittest.TestCase):
        def test_single_element(self):
            head = create_linked_list([1])
            self.assertEqual(middle_of_linked_list(head).val, 1)

        def test_odd_length(self):
            head = create_linked_list([1, 2, 3, 4, 5])
            self.assertEqual(middle_of_linked_list(head).val, 3)

        def test_even_length(self):
            head = create_linked_list([1, 2, 3, 4, 5, 6])
            # For even length, returns second middle (4)
            self.assertEqual(middle_of_linked_list(head).val, 4)

        def test_two_elements(self):
            head = create_linked_list([1, 2])
            self.assertEqual(middle_of_linked_list(head).val, 2)

    # Demo
    demo = [1, 2, 3, 4, 5]
    head = create_linked_list(demo)
    print(f"Linked List: {linked_list_to_array(head)}")
    print(f"Middle element: {middle_of_linked_list(head).val}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
