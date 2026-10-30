# 📘 Linked List — Hard 02
# Topic: Merge Sort on Linked List
# Approach: Divide and conquer (merge sort)
# Time: O(n log n) | Space: O(log n) for recursion stack

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


def sort_list(head):
    """
    Sorts a linked list using merge sort.
    Returns the sorted linked list's head.
    """
    # Base case: empty or single node
    if not head or not head.next:
        return head

    # Step 1: Find middle using fast/slow pointers
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Split the list into two halves
    mid = slow.next
    slow.next = None

    # Step 3: Recursively sort both halves
    left = sort_list(head)
    right = sort_list(mid)

    # Step 4: Merge the sorted halves
    return merge_sorted_lists(left, right)


def merge_sorted_lists(l1, l2):
    """Helper function to merge two sorted linked lists."""
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

    tail.next = l1 if l1 else l2
    return dummy.next


def sort_list_iterative(head):
    """
    Sorts a linked list using iterative (bottom-up) merge sort.
    O(1) extra space (no recursion).
    """
    if not head or not head.next:
        return head

    # Get length of the list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    dummy = ListNode(0)
    dummy.next = head

    # Bottom-up merge sort
    step = 1
    while step < length:
        prev = dummy
        current = dummy.next

        while current:
            left = current
            right = split_list(left, step)
            current = split_list(right, step)
            prev = merge_and_connect(prev, left, right)

        step *= 2

    return dummy.next


def split_list(head, step):
    """
    Splits the list into two parts:
    - First part: at most `step` nodes
    - Second part: starts after the first part
    Returns the head of the second part.
    """
    current = head
    for _ in range(step - 1):
        if current and current.next:
            current = current.next
        else:
            break

    second = current.next if current else None
    if current:
        current.next = None
    return second


def merge_and_connect(prev, left, right):
    """
    Merges left and right lists, connects to prev.
    Returns the tail of the merged list.
    """
    tail = prev
    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left else right
    while tail.next:
        tail = tail.next
    return tail


if __name__ == "__main__":
    import unittest

    class TestSortLinkedList(unittest.TestCase):
        def test_basic(self):
            head = create_linked_list([4, 2, 1, 3])
            sorted_head = sort_list(head)
            self.assertEqual(linked_list_to_array(sorted_head), [1, 2, 3, 4])

        def test_already_sorted(self):
            head = create_linked_list([1, 2, 3, 4])
            sorted_head = sort_list(head)
            self.assertEqual(linked_list_to_array(sorted_head), [1, 2, 3, 4])

        def test_reverse_order(self):
            head = create_linked_list([4, 3, 2, 1])
            sorted_head = sort_list(head)
            self.assertEqual(linked_list_to_array(sorted_head), [1, 2, 3, 4])

        def test_unsorted(self):
            head = create_linked_list([5, 1, 1, 2, 0, 0])
            sorted_head = sort_list(head)
            self.assertEqual(linked_list_to_array(sorted_head), [0, 0, 1, 1, 2, 5])

    # Demo
    demo = [4, 2, 1, 3]
    head = create_linked_list(demo)
    print(f"Original: {linked_list_to_array(head)}")
    sorted_head = sort_list(head)
    print(f"Sorted: {linked_list_to_array(sorted_head)}")
    print("Running unit tests...")
    unittest.main(verbosity=0)
