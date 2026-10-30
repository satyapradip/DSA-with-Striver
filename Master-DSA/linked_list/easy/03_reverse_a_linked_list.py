# 📘 Linked List — Easy 03
# Topic: Linked List Reversal — Reverse a Linked List
# Approach: Iterative reversal with 3 pointers
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


def reverse_linked_list(head):
    """
    Reverses a linked list iteratively.
    Returns the new head.
    """
    prev = None
    current = head
    while current:
        next_node = current.next  # Save next
        current.next = prev       # Reverse pointer
        prev = current             # Move prev forward
        current = next_node        # Move current forward
    return prev  # New head


def reverse_linked_list_recursive(head):
    """
    Reverses a linked list recursively.
    Returns the new head.
    """
    if not head or not head.next:
        return head
    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def reverse_in_groups(head, k):
    """
    Reverses the linked list in groups of k nodes.
    """
    if not head or k == 1:
        return head

    def get_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def reverse_group(start, k):
        prev = None
        current = start
        count = 0
        while current and count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1
        return prev, current

    length = get_length(head)
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy

    while length >= k:
        group_start = prev_group_end.next
        new_group_head, next_group_start = reverse_group(group_start, k)
        prev_group_end.next = new_group_head
        group_start.next = next_group_start
        prev_group_end = group_start
        length -= k

    return dummy.next


if __name__ == "__main__":
    import unittest

    class TestReverseLinkedList(unittest.TestCase):
        def test_basic(self):
            arr = [1, 2, 3, 4, 5]
            head = create_linked_list(arr)
            reversed_head = reverse_linked_list(head)
            self.assertEqual(linked_list_to_array(reversed_head), [5, 4, 3, 2, 1])

        def test_already_reversed(self):
            arr = [1]
            head = create_linked_list(arr)
            reversed_head = reverse_linked_list(head)
            self.assertEqual(linked_list_to_array(reversed_head), [1])

        def test_empty(self):
            head = create_linked_list([])
            reversed_head = reverse_linked_list(head)
            self.assertIsNone(reversed_head)

        def test_reverse_in_groups(self):
            arr = [1, 2, 3, 4, 5]
            head = create_linked_list(arr)
            new_head = reverse_in_groups(head, 2)
            self.assertEqual(linked_list_to_array(new_head), [2, 1, 4, 3, 5])

    # Demo
    demo = [1, 2, 3, 4, 5]
    head = create_linked_list(demo)
    print(f"Original: {linked_list_to_array(head)}")
    print(f"Reversed: {linked_list_to_array(reverse_linked_list(head))}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
