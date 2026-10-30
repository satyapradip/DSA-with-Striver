# 📘 Linked List — Easy 01
# Topic: Singly Linked List Basics — Node & Basic Operations
# Approach: Node structure + manipulation

class ListNode:
    """Singly linked list node."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr):
    """
    Creates a linked list from a Python list.
    """
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head):
    """
    Converts a linked list to a Python list.
    """
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def get_length(head):
    """
    Returns the length of the linked list.
    """
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count


def search_element(head, target):
    """
    Searches for a target element in the linked list.
    Returns True if found, False otherwise.
    """
    current = head
    while current:
        if current.val == target:
            return True
        current = current.next
    return False


def insert_at_beginning(head, val):
    """
    Inserts a new node with value `val` at the beginning.
    """
    new_node = ListNode(val)
    new_node.next = head
    return new_node


def insert_at_end(head, val):
    """
    Inserts a new node with value `val` at the end.
    """
    new_node = ListNode(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head


def delete_at_beginning(head):
    """
    Deletes the first node and returns the new head.
    """
    if not head:
        return None
    return head.next


def delete_at_end(head):
    """
    Deletes the last node and returns the new head.
    """
    if not head:
        return None
    if not head.next:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head


if __name__ == "__main__":
    import unittest

    class TestLinkedListBasics(unittest.TestCase):
        def test_create_and_traverse(self):
            head = create_linked_list([1, 2, 3, 4, 5])
            self.assertEqual(linked_list_to_array(head), [1, 2, 3, 4, 5])

        def test_length(self):
            head = create_linked_list([1, 2, 3])
            self.assertEqual(get_length(head), 3)

        def test_search(self):
            head = create_linked_list([1, 2, 3])
            self.assertTrue(search_element(head, 2))
            self.assertFalse(search_element(head, 5))

        def test_insert_at_beginning(self):
            head = create_linked_list([1, 2, 3])
            head = insert_at_beginning(head, 0)
            self.assertEqual(linked_list_to_array(head), [0, 1, 2, 3])

        def test_insert_at_end(self):
            head = create_linked_list([1, 2, 3])
            head = insert_at_end(head, 4)
            self.assertEqual(linked_list_to_array(head), [1, 2, 3, 4])

        def test_delete_at_beginning(self):
            head = create_linked_list([1, 2, 3])
            head = delete_at_beginning(head)
            self.assertEqual(linked_list_to_array(head), [2, 3])

        def test_delete_at_end(self):
            head = create_linked_list([1, 2, 3])
            head = delete_at_end(head)
            self.assertEqual(linked_list_to_array(head), [1, 2])

    # Demo
    demo = [1, 2, 3, 4, 5]
    head = create_linked_list(demo)
    print(f"Original: {linked_list_to_array(head)}")
    head = insert_at_beginning(head, 0)
    print(f"After insert at beginning: {linked_list_to_array(head)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
