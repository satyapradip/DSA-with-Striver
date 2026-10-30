# 📘 Linked List — Medium 02
# Topic: Two Pointers (Sorted) — Remove Nth Node from End
# Approach: Two pointers with dummy node
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


def remove_nth_from_end(head, n):
    """
    Removes the Nth node from the end of the list.
    Returns the head of the modified list.
    """
    dummy = ListNode(0, head)  # Dummy node simplifies edge cases
    slow = fast = dummy

    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # Skip the nth node from end
    slow.next = slow.next.next

    return dummy.next


def remove_nth_from_end_brute(head, n):
    """
    Removes the Nth node from the end using a two-pass approach.
    """
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # If removing the head
    if n == length:
        return head.next

    # Find the node before the one to remove
    target_pos = length - n
    current = head
    for _ in range(target_pos - 1):
        current = current.next

    current.next = current.next.next
    return head


if __name__ == "__main__":
    import unittest

    class TestRemoveNthFromEnd(unittest.TestCase):
        def test_remove_from_end(self):
            head = create_linked_list([1, 2, 3, 4, 5])
            new_head = remove_nth_from_end(head, 2)
            self.assertEqual(linked_list_to_array(new_head), [1, 2, 3, 5])

        def test_remove_head(self):
            head = create_linked_list([1, 2, 3, 4, 5])
            new_head = remove_nth_from_end(head, 5)
            self.assertEqual(linked_list_to_array(new_head), [2, 3, 4, 5])

        def test_remove_single_element(self):
            head = create_linked_list([1])
            new_head = remove_nth_from_end(head, 1)
            self.assertIsNone(new_head)

        def test_remove_second_last(self):
            head = create_linked_list([1, 2, 3, 4, 5])
            new_head = remove_nth_from_end(head, 2)
            self.assertEqual(linked_list_to_array(new_head), [1, 2, 3, 5])

    # Demo
    demo = [1, 2, 3, 4, 5]
    n = 2
    head = create_linked_list(demo)
    print(f"Original: {linked_list_to_array(head)}")
    print(f"Remove {n}th from end: {linked_list_to_array(remove_nth_from_end(head, n))}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
