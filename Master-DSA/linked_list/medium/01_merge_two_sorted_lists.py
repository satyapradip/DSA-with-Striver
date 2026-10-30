# 📘 Linked List — Medium 01
# Topic: Two Pointers (Sorted) — Merge Two Sorted Linked Lists
# Approach: Two-pointer merge
# Time: O(n + m) | Space: O(1)

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


def merge_two_sorted_lists(l1, l2):
    """
    Merges two sorted linked lists into one sorted list.
    Returns the head of the merged list.
    """
    dummy = ListNode(0)
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Attach remaining nodes
    tail.next = l1 if l1 else l2
    return dummy.next


def merge_two_sorted_lists_recursive(l1, l2):
    """
    Merges two sorted linked lists recursively.
    """
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val < l2.val:
        l1.next = merge_two_sorted_lists_recursive(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_sorted_lists_recursive(l1, l2.next)
        return l2


if __name__ == "__main__":
    import unittest

    class TestMergeTwoSortedLists(unittest.TestCase):
        def test_basic(self):
            l1 = create_linked_list([1, 3, 5])
            l2 = create_linked_list([2, 4, 6])
            merged = merge_two_sorted_lists(l1, l2)
            self.assertEqual(linked_list_to_array(merged), [1, 2, 3, 4, 5, 6])

        def test_one_empty(self):
            l1 = create_linked_list([1, 2, 3])
            l2 = create_linked_list([])
            merged = merge_two_sorted_lists(l1, l2)
            self.assertEqual(linked_list_to_array(merged), [1, 2, 3])

        def test_both_empty(self):
            merged = merge_two_sorted_lists(None, None)
            self.assertIsNone(merged)

        def test_recursive(self):
            l1 = create_linked_list([1, 3, 5])
            l2 = create_linked_list([2, 4, 6])
            merged = merge_two_sorted_lists_recursive(l1, l2)
            self.assertEqual(linked_list_to_array(merged), [1, 2, 3, 4, 5, 6])

    # Demo
    l1 = create_linked_list([1, 3, 5])
    l2 = create_linked_list([2, 4, 6])
    print(f"List 1: {linked_list_to_array(l1)}")
    print(f"List 2: {linked_list_to_array(l2)}")
    merged = merge_two_sorted_lists(l1, l2)
    print(f"Merged: {linked_list_to_array(merged)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
